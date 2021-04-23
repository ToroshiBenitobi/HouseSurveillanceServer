from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order

surveillanceblue = Blueprint('surveillanceblue', __name__)
camerautl = None
global_frame = None
SAVE_PATH = "/home/pi/Videos/Test"  # will be created if doesnt exist
if True:
    from App.tools.camerautl import VideoCamera
else:
    from App.toolsvirtual.camerautl import VideoCamera


@surveillanceblue.route('/surveillance/camera', methods=['POST', 'GET'])
def camera():
    return render_template('surveillance/camera.html')




def gen():
    global camerautl
    global global_frame

    if camerautl is None:
        camerautl = VideoCamera()

    while True:
        frame = camerautl.get_frame()

        if frame is not None:
            global_frame = frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')


@surveillanceblue.route('/surveillance/streaming')
def streaming():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@surveillanceblue.route('/surveillance/recordstatus', methods=['POST'])
def record_status():
    if camerautl is None:
        video_camera = VideoCamera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        video_camera.start_record()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        return jsonify(result="stopped")
