from flask_apscheduler import APScheduler
from App.tools.sensorutl import sensorutl
from App.tools.camerautl import VideoCamera
from App.views.surveillance import record_status_without_json
from App import create_app
scheduler = APScheduler()
abnormally = False
APP = None

def get_app():
    global APP
    APP = APP if APP is not None else create_app(args)


def check_sensor():
    get_app()
    with APP.app_context:
        global abnormally
        temperature = sensorutl.temperature()
        humidity = sensorutl.humidity()
        print(temperature, humidity)
        if temperature < 27 and humidity < 60 and not abnormally:
            print(1)
            pass
        elif (temperature >= 27 or humidity >= 60) and not abnormally:
            print(2)
            record_status_without_json(status=True)
            abnormally = True
        elif temperature < 27 and humidity < 60 and abnormally:
            print(3)
            record_status_without_json(status=False)
            abnormally = False
        elif (temperature >= 27 or humidity >= 60) and abnormally:
            print(4)
            pass