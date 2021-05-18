from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response, jsonify
from App.models import db, Order
import json
import datetime
from App.models import db, User, Video

surveillanceblue = Blueprint('surveillanceblue', __name__)
camerautl = None
global_frame = None
SAVE_PATH = "/home/pi/Videos/Test"  # will be created if doesnt exist
from App.tools.camerautl import VideoCamera


@surveillanceblue.route('/surveillance/camera', methods=['POST', 'GET'])
def camera():
    return render_template('surveillance/camera.html')


@surveillanceblue.route('/surveillance/managefacedata', methods=['POST', 'GET'])
def manage_face_data():
    return render_template('surveillance/managefacedata.html')


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
    global camerautl
    if camerautl is None:
        camerautl = VideoCamera()

    json = request.get_json()

    status = json['status']

    if status == "true":
        camerautl.start_record()
        return jsonify(result="started")
    else:
        save_path = camerautl.stop_record()
        item = session.get('user')
        video = Video()
        video.videoid = video.query.count() + 1
        video.videoname = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        video.savepath = save_path
        if item is not None:
            userid = item.get('id')
            video.userid = userid
        db.session.add(video)
        db.session.commit()
        return jsonify(result="stopped", save_path=save_path)


@surveillanceblue.route('/surveillance/downloadvideo', methods=['POST', 'GET'])
def download_video():
    item = session.get('user')
    userid = item.get('id')
    videos = Video.query.filter(Video.userid == userid).all()
    print(videos)
    return render_template('/surveillance/downloadvideo.html', videos=videos)


@surveillanceblue.route('/surveillance/faceupload', methods=['POST', 'GET'])
def upload_face():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            contents = file.read()
            filename = file.filename
            # creating a folder if there is no one yet
            # saving file with new name in exact folder
            upload_folder = 'App/static/faces/'
            file.save(upload_folder+filename)
            session['msg'] = '成功'
        else:
            session['msg'] = '失败'
    return render_template('/surveillance/uploadfacesuccess.html')
