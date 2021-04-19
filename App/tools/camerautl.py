#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np

class Streaming(object):
    def __init__(self, angle = 0):
        self.vs = PiVideoStream().start()
        self.angle = angle
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def rotate(self, frame):
        return np.rot90(frame, self.angle)

    def get_frame(self):
        frame = self.rotate(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()