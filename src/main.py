# import cv2
# import numpy as np
# from video_capture import VideoCapture
# from object_detection import ObjectDetector
# from distance_calculation import DistanceCalculator
# from audio_output import AudioOutput

# def main():
#     # Initialize VideoCapture with DroidCam URL
#     # Replace '192.168.0.100' with your phone's IP address
#     # video_capture = VideoCapture('http://192.168.29.242.4747/video')
#     video_capture = VideoCapture(ip_address='192.168.29.242', port=4747)

    
#     object_detector = ObjectDetector()
#     distance_calculator = DistanceCalculator()
#     audio_output = AudioOutput()

#     while video_capture.is_opened():
#         frame = video_capture.get_frame()
#         if frame is None:
#             break

#         detections = object_detector.detect(frame)
#         for detection in detections:
#             class_id, confidence, bbox = detection
#             x, y, w, h = bbox
            
#             # Draw bounding box
#             color = object_detector.get_color(class_id)
#             cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
#             # Display label
#             object_name = object_detector.get_class_name(class_id)
#             label = f"{object_name} {confidence:.2f}"
#             cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
#             # Calculate distance
#             distance = distance_calculator.calculate(w, h)
            
#             # Check if distance is below threshold
#             if distance < distance_calculator.threshold:
#                 audio_output.speak(f"{object_name} ahead at {distance:.2f} meters")

#         cv2.imshow("Visual Assistant", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()

import cv2
import numpy as np
from video_capture import VideoCapture
from object_detection import ObjectDetector
from distance_calculation import DistanceCalculator
from audio_output import AudioOutput

def main():
    video_capture = VideoCapture(0)  # 0 is usually the default webcam
    object_detector = ObjectDetector()
    distance_calculator = DistanceCalculator()
    audio_output = AudioOutput()

    while video_capture.is_opened():
        frame = video_capture.get_frame()
        if frame is None:
            break

        detections = object_detector.detect(frame)
        for detection in detections:
            class_id, confidence, bbox = detection
            x, y, w, h = bbox
            
            # Draw bounding box
            color = object_detector.get_color(class_id)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
            # Display label
            object_name = object_detector.get_class_name(class_id)
            label = f"{object_name} {confidence:.2f}"
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # Calculate distance
            distance = distance_calculator.calculate(w, h)
            
            # Check if distance is below threshold
            if distance < distance_calculator.threshold:
                audio_output.speak(f"{object_name} ahead at {distance:.2f} meters")

        cv2.imshow("Visual Assistant", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()