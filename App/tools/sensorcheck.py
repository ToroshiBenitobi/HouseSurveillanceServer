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
AUTO_ABNORMALLY_RESET = True
TEM_LOW_LIMIT = 28
TEM_HIGH_LIMIT = 28
HUM_LOW_LIMIT = 60
HUM_HIGH_LIMIT = 60
ENTER_NOT_ALLOWED = True
def check_sensor():
    with scheduler.app.app_context():
        global abnormally
        temperature = sensorutl.temperature()
        humidity = sensorutl.humidity()
        is_detected = sensorutl.is_detected()
        print(temperature, humidity)
        if not abnormally:
            msg = ''
            if temperature > TEM_HIGH_LIMIT:
                msg += '温度太高、'
            if temperature < TEM_LOW_LIMIT:
                msg += '温度太低、'
            if humidity > HUM_HIGH_LIMIT:
                msg += '湿度太高、'
            if humidity < HUM_LOW_LIMIT:
                msg += '湿度太高、'
            if is_detected and ENTER_NOT_ALLOWED:
                msg += '探测到陌生人闯入、'
            if len(msg) > 0:
                msg = '【宿舍智能管理系统】警告，宿舍检测到如下异常：\n' + msg[:-1] + '。\n请立即登录系统查看情况。'
                print(msg)



def reset():
    with scheduler.app.app_context():
        global abnormally
        if AUTO_ABNORMALLY_RESET:
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