from flask_apscheduler import APScheduler
from App.tools.sensorutl import sensorutl
from App.tools.camerautl import VideoCamera
from App.views.surveillance import camerautl

scheduler = APScheduler()
abnormally = False


def check_sensor():
    global abnormally
    temperature = sensorutl.temperature()
    humidity = sensorutl.humidity()
    print(temperature, humidity)
    if temperature < 27 and humidity < 60 and not abnormally:
        pass
    elif (temperature >= 27 or humidity >= 60) and not abnormally:
        record_status_without_json(status=True)
        abnormally = True
    elif temperature < 27 and humidity < 60 and abnormally:
        record_status_without_json(status=False)
        abnormally = False
    elif (temperature >= 27 or humidity >= 60) and abnormally:
        pass


def record_status_without_json(status):
    global camerautl
    if camerautl is None:
        camerautl = VideoCamera()

    if status:
        camerautl.start_record()
        return 'Start'
    else:
        save_path = camerautl.stop_record()
        return 'Stop'
