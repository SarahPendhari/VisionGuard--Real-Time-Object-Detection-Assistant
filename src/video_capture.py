# import cv2
# import numpy as np
# import time

# class VideoCapture:
#     def __init__(self, ip_address='192.168.29.242', port=4747):
#         self.url = f'http://{ip_address}:{port}/video'
#         self.cap = cv2.VideoCapture(self.url)
        
#         # Allow the camera to warm up
#         time.sleep(2)
        
#         if not self.cap.isOpened():
#             raise IOError(f"Cannot open URL {self.url}")

#         # Set resolution (optional)
#         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#     def get_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             return frame
#         return None

#     def release(self):
#         self.cap.release()

#     def is_opened(self):
#         return self.cap.isOpened()

#     def get_fps(self):
#         return self.cap.get(cv2.CAP_PROP_FPS)

#     def get_frame_size(self):
#         width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         return (width, height)

import cv2

class VideoCapture:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def release(self):
        self.cap.release()

    def is_opened(self):
        return self.cap.isOpened()