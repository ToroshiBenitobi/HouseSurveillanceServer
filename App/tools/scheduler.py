from flask_apscheduler import APScheduler
from App.tools.sensorutl import sensorutl
from App.tools.camerautl import VideoCamera
from App.views.surveillance import record_status_without_json
from App import create_app
from app import env
scheduler = APScheduler()
abnormally = False
APP = None
