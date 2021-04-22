from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
surveillanceblue = Blueprint('surveillanceblue', __name__)
if True:
    from App.tools.camerautl import camerautl
else:
    from App.toolsvirtual.camerautl import camerautl

@surveillanceblue.route('/surveillance/camera', methods=['POST', 'GET'])
def camera():
    return render_template('surveillance/camera.html')


def gen(camerautl):
    # get camera frame
    while True:
        frame = camerautl.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@surveillanceblue.route('/surveillance/streaming')
def video_feed():
    return Response(gen(camerautl),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@surveillanceblue.route('/surveillance/savevideo')
def save_video():
    camerautl.save_frames()
    return 'save'