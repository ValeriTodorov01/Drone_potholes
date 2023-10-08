# Drone Fire and Pothole Detection Repository

This repository contains code and resources for a drone equipped with fire detection and pothole/object detection capabilities. The repository is organized into two main sub-folders:

1. **fire-detection**: This folder contains the logic and code for fire detection using Python. The fire detection algorithm is designed to run on the drone's onboard computer and identify the presence of fires in the drone's surroundings.

2. **pothole-and-object-detection-main**: This folder contains the logic and code for pothole and object detection using Python. The algorithm is designed to help the drone identify potholes and other objects on the ground, ensuring safe navigation and obstacle avoidance.

## Repository Structure

Here's an overview of the repository's structure:  (needs to be finished)

```
drone-fire-pothole-detection/
│
├── fire-detection/
│   ├── README.md
│   ├── fire_detection.py
│   ├── ...
│   └── data/
│       ├── .....
│       ├── ...
│
├── pothole-detection-main/
│   ├── README.md
│   ├── pothole_detection.py
│   ├── object_detection.py
│   ├── ...
│   └── data/
│       ├── ...
│       ├── ...
│       ├── ...
│
├── LICENSE
└── .gitignore
```

## Getting Started

To set up and use this repository, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

   ```bash
   git clone https://github.com/your-username/drone-fire-pothole-detection.git
   ```

2. **Fire Detection**: If you are interested in the fire detection functionality, navigate to the `fire-detection` folder, and follow the instructions provided in the README.md file within that folder.

3. **Pothole and Object Detection**: If you want to work with the pothole and object detection functionality, navigate to the `pothole-detection-main` folder and refer to the README.md file for detailed instructions on how to set up and use the detection capabilities.

4. **Data Models**: The `data` sub-folder within each detection module contains pre-trained models (e.g., `trained_model.pth` and `trained_pothole_model.pth`). These models are used by the respective detection modules for inference. You may need to download or train these models according to your requirements.

## License

This repository is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions to this project are welcome! If you have ideas, bug fixes, or improvements, please feel free to open issues or pull requests.

## Contact

If you have any questions or need further assistance, please feel free to contact us at [valeri.m.todorov.2020@elsys-bg.org].
