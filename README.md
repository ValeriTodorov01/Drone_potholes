# Safty drone

This repository contains code and resources for a drone equipped with fire detection and pothole/object detection capabilities. The repository is organized into two main sub-folders:

1. **Fire-Detection-System**: This folder contains the logic and code for fire detection using Python. The fire detection algorithm is designed to run on the drone's onboard computer and identify the presence of fires in the drone's surroundings.

2. **pothole-and-object-detection**: This folder contains the logic and code for pothole and object detection using Python. The algorithm is designed to help the drone identify potholes and other objects on the ground, ensuring safe navigation and obstacle avoidance.

## Repository Structure

Here's an overview of the repository's structure: (needs to be finished)

```
Safty drone/
│
├── Fire-Detection-System/
│   ├── Alarm Sound.mp3        //an alarm for signalling that fire is detected
│   ├── fire.mp4               //an example video for fire
│   └── fire_detector.py      //the code for fire detection
│
├── pothole-and-object-detection/
│   ├── object_recognition/      //a folder containing the main files for the object detection AI
│   ├── pothole_coordinates/     //a folder containing imgs and txt files for found potholes
│   ├── pothole_img/             //a folder containing raw imgs
│   ├── project_files/           //a folder containing the main files for the pothole detection AI
│   ├── training_files/          //a folder containing files for the data processing
│   ├── camera_video.py          //file for live detection from local camera or from other video source
│   ├── pothole_by_image.py      //file only for finding potholes in a given image
│   └── (some examples for testing)
│
├── main.py                      //the main file that should be run
|
├── requirements.txt             //file with the needed libraries for the project
│
├── LICENSE
└── .gitignore
```

## Getting Started

To set up and use this repository, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

   ```bash
   git clone https://github.com/ValeriTodorov01/Drone_potholes.git
   ```

2. **Fire Detection**: If you are interested in the fire detection functionality, navigate to the `fire-detection` folder, and follow the instructions provided in the README.md file within that folder. (soon)

3. **Pothole and Object Detection**: If you want to work with the pothole and object detection functionality, navigate to the `pothole-and-object-detection-main` folder and refer to the README.md file for detailed instructions on how to set up and use the detection capabilities. (soon)

4. **Requirements**: Navigate to requirements.txt for more info on what you need to start the project.

5. **Full functionality**: If you want to work with the full ponential of the code navigate to the main.py.

## License

This repository is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for details. (soon)

## Contributing

Contributions to this project are welcome! If you have ideas, bug fixes, or improvements, please feel free to open issues or pull requests.

## Contact

If you have any questions or need further assistance, please feel free to contact us at [valeri.m.todorov.2020@elsys-bg.org] or [borislav.b.milanov.2020@elsys-bg.org].
