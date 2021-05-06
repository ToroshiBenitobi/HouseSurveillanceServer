from App.tools.sensorutl import sensorutl
from App.views.surveillance import record_status_without_json
from App.tools.scheduler import scheduler
abnormally = False
TEM_LIMIT = 28
HUM_LIMIT = 60
def check_sensor():
    with scheduler.app.app_context():
        global abnormally, TEM_LIMIT, HUM_LIMIT
        temperature = sensorutl.temperature()
        humidity = sensorutl.humidity()
        print(temperature, humidity)
        if temperature < TEM_LIMIT and humidity < HUM_LIMIT and not abnormally:
            print(1)
            pass
        elif (temperature >= TEM_LIMIT or humidity >= HUM_LIMIT) and not abnormally:
            print(2)
            record_status_without_json(status=True)
            abnormally = True
        elif temperature < TEM_LIMIT and humidity < HUM_LIMIT and abnormally:
            print(3)
            record_status_without_json(status=False)
            abnormally = False
        elif (temperature >= TEM_LIMIT or humidity >= HUM_LIMIT) and abnormally:
            print(4)
            pass