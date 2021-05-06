from App.tools.sensorutl import sensorutl
from App.views.surveillance import camerautl
from App.tools.scheduler import scheduler
from App.tools.camerautl import VideoCamera
from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response, jsonify
from App.models import db, Order
import json
import datetime
from App.models import db, User, Video
abnormally = False
TEM_LIMIT = 28
HUM_LIMIT = 60
def check_sensor():
    with scheduler.app.app_context():
        global abnormally, TEM_LIMIT, HUM_LIMIT
        temperature = sensorutl.temperature()
        humidity = sensorutl.humidity()
        print(temperature, humidity)
        if not abnormally:
            record_status_without_json(status=True)
            abnormally = True
        else:
            record_status_without_json(status=False)
            abnormally = False
        # if temperature < TEM_LIMIT and humidity < HUM_LIMIT and not abnormally:
        #     print(1)
        #     pass
        # elif (temperature >= TEM_LIMIT or humidity >= HUM_LIMIT) and not abnormally:
        #     print(2)
        #     record_status_without_json(status=True)
        #     abnormally = True
        # elif temperature < TEM_LIMIT and humidity < HUM_LIMIT and abnormally:
        #     print(3)
        #     record_status_without_json(status=False)
        #     abnormally = False
        # elif (temperature >= TEM_LIMIT or humidity >= HUM_LIMIT) and abnormally:
        #     print(4)
        #     pass



def record_status_without_json(status):
    global camerautl
    if camerautl is None:
        camerautl = VideoCamera()

    if status:
        camerautl.start_record()
        return True
    else:
        save_path = camerautl.stop_record()
        item = None
        video = Video()
        video.videoid = video.query.count() + 1
        video.videoname = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        video.savepath = save_path
        if item is not None:
            userid = item.get('id')
            video.userid = userid
        db.session.add(video)
        db.session.commit()
        return False