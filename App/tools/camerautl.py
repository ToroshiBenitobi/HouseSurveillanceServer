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
import datetime
from App.tools.facerecognitionutl import load_known_face, recognize_face, draw_face_frame


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

# class RecordingThread(threading.Thread):
#     def __init__(self, name, camera):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.isRunning = True
#         self.cap = camera
#         fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#         self.out = cv2.VideoWriter('App/static/savevideos/video.avi', fourcc, 20.0, (640, 480))
#
#     def run(self):
#         while self.isRunning:
#             ret, frame = self.cap.read()
#             if ret:
#                 self.out.write(frame)
#
#         self.out.release()
#
#     def stop(self):
#         self.isRunning = False
#
#     def __del__(self):
#         self.out.release()


class VideoCamera(object):
    def __init__(self, root_path="App/static/savevideos/"):
        # 打开摄像头， 0代表笔记本内置摄像头
        self.cap = cv2.VideoCapture(0)
        self.root_path = root_path
        self.video_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        self.save_path = self.root_path + self.video_name + '.avi'
        # 初始化视频录制环境
        self.is_record = False
        self.out = None
        self.face_locations = []
        self.face_names = []
        self.known_face_names, self.known_face_encodings = load_known_face()

    # 退出程序释放摄像头
    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # 图像反转
            cv2.flip(frame, 0)
            # 人脸识别
            self.face_locations, self.face_names = recognize_face(frame, self.known_face_encodings, self.known_face_names)
            frame = draw_face_frame(frame, self.face_locations, self.face_names)
            ret, jpeg = cv2.imencode('.jpg', frame)

            # 视频录制
            if self.is_record:
                if self.out == None:
                    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
                    self.out = cv2.VideoWriter(self.save_path, fourcc, 24.0, (640, 480))

                ret, frame = self.cap.read()
                if ret:
                    self.out.write(frame)
            else:
                if self.out != None:
                    self.out.release()
                    self.out = None

            return jpeg.tobytes()

        else:
            return None

    def start_record(self):
        self.video_name = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        self.save_path = self.root_path + self.video_name + '.avi'
        self.is_record = True

    def stop_record(self):
        self.is_record = False
        path = '/static/savevideos/' + self.video_name + '.avi'
        return path

        # if self.recordingThread != None:
        #     self.recordingThread.stop()
