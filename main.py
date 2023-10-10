#importing necessary libraries
import cv2 as cv
import time
import geocoder
import os
import numpy as np
import playsound
import threading


#reading label name from obj.names file
class_name = []
with open(os.path.join("pothole-and-object-detection/project_files",'obj.names'), 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]

#importing model weights and config file
#defining the model parameters
net1 = cv.dnn.readNet('pothole-and-object-detection/project_files/yolov4_tiny.weights', 'pothole-and-object-detection/project_files/yolov4_tiny.cfg')
net1.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net1.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
model1 = cv.dnn_DetectionModel(net1)
model1.setInputParams(size=(640, 480), scale=1/255, swapRB=True)


classNames_obj_detect = []
classFile = 'pothole-and-object-detection/object_recognition/coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'pothole-and-object-detection/object_recognition/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightPath = 'pothole-and-object-detection/object_recognition/frozen_inference_graph.pb'

net2 = cv.dnn_DetectionModel(weightPath, configPath)
net2.setInputSize(320, 320)
net2.setInputScale(1.0/127.5)
net2.setInputMean((127.5, 127.5, 127.5))
net2.setInputSwapRB(True)

#defining the video source (0 for camera or file name for video)
#cap = cv.VideoCapture(0)
cap = cv.VideoCapture("pothole-and-object-detection/DJI_0664.mp4")
width  = cap.get(3)
height = cap.get(4)

#result = cv.VideoWriter('result.avi',                                  for result video
#                         cv.VideoWriter_fourcc(*'MJPG'),
#                         10,(int(width),int(height)))




#defining parameters for result saving and get coordinates
#defining initial values for some parameters in the script
g = geocoder.ip('me')
result_path = "pothole-and-object-detection/pothole_coordinates"
starting_time = time.time()
Conf_threshold = 0.5
NMS_threshold = 0.4
frame_counter = 0
i = 0
b = 0


#defining parameters and function for fire detection
Alarm_Status = False
Fire_Reported = 0
play_pause = False
cap_fire = cv.VideoCapture("Fire-Detection-System/fire.mp4")

def play_alarm_sound_function():
	while play_pause:
		playsound.playsound('Fire-Detection-System/Alarm Sound.mp3',True)


#detection loop
while True:
    ret, frame = cap.read()
    frame_counter += 1
    if ret == False:
        break
    #analysis the stream with detection model
    classes, scores, boxes = model1.detect(frame, Conf_threshold, NMS_threshold)
    for (classid, score, box) in zip(classes, scores, boxes):
        label = "pothole"
        x, y, w, h = box
        recarea = w*h
        area = width*height
        #drawing detection boxes on frame for detected potholes and saving coordinates txt and photo
        if(len(scores)!=0 and scores[0]>=0.7):
            if((recarea/area)<=0.1 and box[1]<600):
                cv.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
                cv.putText(frame, "%" + str(round(scores[0]*100,2)) + " " + label, (box[0], box[1]-10),cv.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

    #analysing for fire
    (grabbed, frame_fire) = cap_fire.read()
    if not grabbed:
        break
    frame_fire = cv.resize(frame_fire, (960, 540))
    blur = cv.GaussianBlur(frame_fire, (21, 21), 0)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
    lower = [18, 50, 50]
    upper = [35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv.inRange(hsv, lower, upper)
    output_fire = cv.bitwise_and(frame_fire, hsv, mask=mask)
    no_red = cv.countNonZero(mask)
    if int(no_red) > 15000:
        Fire_Reported = Fire_Reported + 1
    cv.imshow("output", output_fire)
    if Fire_Reported >= 1:
        if Alarm_Status == False:
            play_pause = True
            threading.Thread(target=play_alarm_sound_function).start()
            Alarm_Status = True

    #writing fps on frame
    endingTime = time.time() - starting_time
    fps = frame_counter/endingTime
    cv.putText(frame, f'FPS: {fps}', (20, 50),
               cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    #showing and saving result
    cv.imshow('frame', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        play_pause = False
        break

    success, img = cap.read()  # read the camera frame
    classIds, confs, bbox = net2.detect(img, confThreshold=0.5)
    if not success:
        break
    else:
        for classId, confidence, box in zip(classIds, confs, bbox):
            # if (classNames[classId - 1] == "bottle"):
            cv.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv.putText(img, classNames[classId - 1], (box[0], box[1] - 20), cv.FONT_HERSHEY_COMPLEX, 1,
                        (0, 255, 0), 2)

        cv.imshow("Output", img)
        cv.waitKey(1)

#end
cap.release()
cv.destroyAllWindows()
