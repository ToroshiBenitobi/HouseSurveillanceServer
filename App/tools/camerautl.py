# Modified by smartbuilds.io
# Date: 27.09.20
# Desc: This scrtipt script..
import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np
from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
import base64
import json
from picamera import PiCamera
import time
import threading
import os
SAVE_PATH = "/home/pi/Videos/Test"  # will be created if doesnt exist

class Streaming(object):
    def __init__(self, save_path='', angle=0):
        self.vs = PiVideoStream(framerate=30).start()
        self.save_path = save_path
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

    def save_frames(self):
        frame = self.rotate(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        i = 0
        path = self.save_path + '{}.jpg'
        while i < 50:
            cv2.imwrite(path.format(i), frame)
            i += 1
            time.sleep(0.5)


camerautl = Streaming(save_path=SAVE_PATH, angle=2)  # flip pi camera if upside down.
