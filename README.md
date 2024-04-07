# Face_Recognation
# Facial Recognition System

This Python script performs facial recognition using the MediaPipe library. It allows users to choose between selecting an image from their PC or using a live webcam feed for facial recognition.

## Prerequisites

- Python 3.x
- OpenCV library (`pip install opencv-python`)
- MediaPipe library (`pip install mediapipe`)

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the directory containing the script (`facial_recognition.py`).

3. Ensure that you have a webcam connected to your computer if you plan to use the live webcam feed option.

4. Run the script by executing the following command in your terminal or command prompt:

5. Follow the on-screen prompts to choose between selecting an image from your PC or using a live webcam feed for facial recognition.

6. If you choose to select an image from your PC, enter the path to the image file when prompted.

7. If you choose to use a live webcam feed, press 'q' to exit the feed.

## Options

- Option 1: Image from PC
- Option 2: Live webcam feed

## Additional Information

- The script uses the MediaPipe library for face detection and facial landmark detection.
- Make sure that the webcam is properly connected and functional if you choose the live webcam feed option.
- Adjust the minimum detection confidence threshold (`min_detection_confidence=0.5`) in the `detect_faces` function to change the sensitivity of face detection.

