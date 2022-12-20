from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from cv2 import VideoCapture

class ActiveCameras(QThread):
    def __init__(self,scan_range):
        self.scan_range = scan_range
        super().__init__()
        
    cameras = Signal(list)
    def run(self):
        for camera in range(int(self.scan_range)):
            capture = VideoCapture(camera)
            valid_cameras = []
            if capture.isOpened():
                valid_cameras.append(camera)
                data=[str(x) for x in valid_cameras]
                self.cameras.emit(data)