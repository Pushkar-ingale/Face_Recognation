import cv2
import mediapipe as mp

# Function to detect faces in the image
def detect_faces(image):
    # Initialize MediaPipe face detection
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    # Run face detection on the input image
    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Draw bounding boxes around detected faces
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(image, bbox, (0, 255, 0), 2)
                
    return image

# Function to choose between image from PC or live webcam feed
def choose_option():
    option = input("Choose an option:\n1. Image from PC\n2. Live webcam feed\nEnter option (1/2): ")
    if option == '1':
        # Load image from PC
        img_path = input("Enter the path to the image file: ")
        image = cv2.imread(img_path)
        if image is None:
            print("Error: Unable to read image file.")
            return
        image = detect_faces(image)
        cv2.imshow("Facial Recognition", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif option == '2':
        # Open webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Unable to open webcam.")
            return
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to capture frame.")
                break
            frame = detect_faces(frame)
            cv2.imshow("Facial Recognition", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Invalid option. Please choose 1 or 2.")

# Call the function to choose the option
if __name__ == "__main__":
    choose_option()
