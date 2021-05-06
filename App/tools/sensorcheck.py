from App.tools.sensorutl import sensorutl
from App.views.surveillance import record_status_without_json
from App.tools.scheduler import scheduler

def check_sensor():
    with scheduler.app.app_context():
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