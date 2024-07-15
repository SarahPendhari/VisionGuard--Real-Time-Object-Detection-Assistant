# VisionGuard: Real-Time Object Detection Assistant

VisionGuard is an advanced real-time object detection system that uses computer vision to identify objects, calculate distances, and provide audio feedback. It's designed to assist users in navigating their environment by detecting potential obstacles and providing timely warnings.

## Features

- Real-time object detection using YOLOv3
- Distance calculation for detected objects
- Audio warnings for close objects
- Support for both laptop webcam and smartphone camera (via DroidCam)
- Visual display with bounding boxes and object labels

## Requirements

- Python 3.7+
- OpenCV
- NumPy
- pyttsx3 (for audio output)
- YOLOv3 weights and configuration files

## Installation

1. Clone this repository
2. Install the requirements
3. Download YOLOv3 weights and configuration files:
- [YOLOv3 weights](https://pjreddie.com/media/files/yolov3.weights)
- [YOLOv3 config](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- [COCO names](https://github.com/pjreddie/darknet/blob/master/data/coco.names)

Place these files in the `models/` and `config/` directories respectively.

## YOLOv3 Weights

Due to file size limitations on GitHub, the YOLOv3 weights file is not included in this repository. Please download it separately:

1. Download the YOLOv3 weights file from [here](https://pjreddie.com/media/files/yolov3.weights)
2. Place the downloaded file in the `models/` directory of your local repository

Note: The YOLOv3 weights file is approximately 236MB.

## Usage

### Using Laptop Webcam

Run the main script: python src/main.py

### Using Smartphone Camera (via DroidCam)

1. Install DroidCam on your smartphone and computer.
2. Connect both devices to the same Wi-Fi network.
3. Open DroidCam on your smartphone and note the IP address and port.
4. Modify the `video_capture.py` file to use the DroidCam URL:

   ```python
   video_capture = VideoCapture('http://YOUR_PHONE_IP:4747/video')

Run the main script:
python src/main.py

## How It Works
VisionGuard uses the YOLOv3 (You Only Look Once version 3) model for object detection. YOLOv3 is a state-of-the-art, real-time object detection system that can detect multiple objects in a single frame with high accuracy.

Video Capture: The system captures video frames from either the laptop webcam or a smartphone camera (via DroidCam).
Object Detection: Each frame is processed by the YOLOv3 model to detect objects. YOLOv3 divides the image into a grid and predicts bounding boxes and class probabilities for each grid cell.
Distance Calculation: The system estimates the distance to detected objects based on their size in the frame.
Visual Feedback: Detected objects are highlighted with bounding boxes and labeled on the display.
Audio Warnings: When objects are detected within a certain threshold distance, the system provides audio warnings using text-to-speech.

Contributing
Contributions to VisionGuard are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
YOLOv3 by Joseph Redmon and Ali Farhadi
OpenCV community
DroidCam for enabling smartphone camera usage
