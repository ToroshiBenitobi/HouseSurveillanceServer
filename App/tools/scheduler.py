from flask_apscheduler import APScheduler
scheduler = APScheduler()

def check_sensor():
    print('check_sensor')