from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
from App.tools.camerautl import camerautl
VID_DIR = "/python/picamera-suiveillance-webserver/"  # will be created if doesnt exist
surveillanceblue = Blueprint('surveillanceblue', __name__)

@surveillanceblue.route('/surveillance/camera', methods=['POST', 'GET'])
def camera():
    return render_template('surveillance/camera.html')


def gen(camera):
    # get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@surveillanceblue.route('/surveillance/streaming')
def video_feed():
    return Response(gen(camerautl),
                    mimetype='multipart/x-mixed-replace; boundary=frame')