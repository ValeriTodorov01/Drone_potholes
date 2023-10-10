#  importing necessary libraries

import cv2
import os

while 1:
    var = int(input("Choose a image between 1 and 5: "))
    print(var)
    if 1 <= var <= 5:
        break
    else:
        print("Wrong input")


# reading test image
img = cv2.imread("pothole-and-object-detection/pothole_img/hole" + str(var) + ".jpg")  # image name

# reading label name from obj.names file
with open(os.path.join("pothole-and-object-detection/project_files", 'obj.names'), 'r') as f:
    classes = f.read().splitlines()

# importing model weights and config file
net = cv2.dnn.readNet('pothole-and-object-detection/project_files/yolov4_tiny.weights',
                      'pothole-and-object-detection/project_files/yolov4_tiny.cfg')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)

# detection 
for (classId, score, box) in zip(classIds, scores, boxes):
    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)

img2 = cv2.resize(img, (1920, 1080))
os.chdir(r'pothole-and-object-detection/pothole_img_found')

cv2.imshow("pothole", img2)
cv2.imwrite("result1"+".jpg", img2)  # result name
cv2.waitKey(0)
cv2.destroyAllWindows()
