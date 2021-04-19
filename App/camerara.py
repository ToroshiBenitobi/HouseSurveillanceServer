HOST="0.0.0.0"
PORT=5000
VID_DIR="/python/picamera-suiveillance-webserver/" # will be created if doesnt exist

import base64
import json
from flask import Flask, render_template, Response, request
from camera import Streaming
from sensors import Sensors
from picamera import PiCamera
import time
import threading
import os

pi_camera = Streaming(angle=2) # flip pi camera if upside down.
pi_censor = Sensors()
# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/streaming')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/sensor-info')
def sensor_info():
    msg = 'Temperature: {:.1f} Humidity: {:.1f} Motion: {}'
    msg = msg.format(pi_censor.temperature(), pi_censor.humidity(), pi_censor.is_detected())
    return msg

@app.route('/start-recording')
def start_recording():
    pass

@app.route('/stop-recording')
def stop_recording():
    pass

@app.route('/get-video')
def get_video():
    pass

if __name__ == '__main__':

    app.run(host=HOST, port=PORT, debug=False)
    while True:
        msg = 'Temperature: {:.1f} Humidity: {:.1f} Motion: {}'
        msg = msg.format(pi_censor.temperature(), pi_censor.humidity(), pi_censor.is_detected())
        print(msg)
        time.sleep(2)
    


