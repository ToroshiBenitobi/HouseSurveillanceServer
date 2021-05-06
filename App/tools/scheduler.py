from flask_apscheduler import APScheduler
scheduler = APScheduler(BackgroundScheduler(timezone="Asia/Shanghai"))

def check_sensor():
    print('check_sensor')