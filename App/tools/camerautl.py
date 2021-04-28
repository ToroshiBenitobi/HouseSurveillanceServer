# Modified by smartbuilds.io
# Date: 27.09.20
# Desc: This scrtipt script..
import cv2
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

# class Streaming(object):
#     def __init__(self, save_path='', angle=0):
#         self.vs = PiVideoStream(framerate=30).start()
#         self.save_path = save_path
#         self.angle = angle
#         time.sleep(2.0)
#
#     def __del__(self):
#         self.vs.stop()
#
#     def rotate(self, frame):
#         return np.rot90(frame, self.angle)
#
#     def get_frame(self):
#         frame = self.rotate(self.vs.read())
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         return jpeg.tobytes()
#
#     def save_frames(self):
#         frame = self.rotate(self.vs.read())
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         i = 0
#         path = self.save_path + '{}.jpg'
#         while i < 10:
#             cv2.imwrite(path.format(i), frame)
#             i += 1
#             time.sleep(0.5)
#
# camerautl = Streaming(save_path=SAVE_PATH, angle=2)  # flip pi camera if upside down.

class RecordingThread(threading.Thread):
    def __init__(self, name, camera):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True
        self.cap = camera
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.out = cv2.VideoWriter('App/static/savevideos/video.avi', fourcc, 20.0, (640, 480))

    def run(self):
        while self.isRunning:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)

        self.out.release()

    def stop(self):
        self.isRunning = False

    def __del__(self):
        self.out.release()


class VideoCamera(object):
    def __init__(self):
        # 打开摄像头， 0代表笔记本内置摄像头
        self.cap = cv2.VideoCapture(0)

        # 初始化视频录制环境
        self.is_record = False
        self.out = None

        # 视频录制线程
        self.recordingThread = None

    # 退出程序释放摄像头
    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()

        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)

            # 视频录制
            if self.is_record:
                print('self.is_record')
                if self.out == None:
                    print('self.out == None')
                    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
                    self.out = cv2.VideoWriter('App/static/savevideos/video001.avi', fourcc, 20.0, (640, 480))

                ret, frame = self.cap.read()
                if ret:
                    print('ret')
                    print(frame.shape)
                    self.out.write(frame)
            else:
                if self.out != None:
                    self.out.release()
                    self.out = None

            return jpeg.tobytes()

        else:
            return None

    def start_record(self):
        self.is_record = True
        # self.recordingThread = RecordingThread("Video Recording Thread", self.cap)
        # self.recordingThread.start()

    def stop_record(self):
        self.is_record = False

        if self.recordingThread != None:
            self.recordingThread.stop()
