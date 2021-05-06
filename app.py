#from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
#app = Flask(__name__)


#@app.route('/')
#def user():
#    return render_template('login.html')


#if __name__ == '__main__':
#    app.run()
#书上的部分：应用主脚本
import os
# 从应用包的构造文件中引入create_app
from App import create_app
# 引入flask-migrate
from flask_migrate import MigrateCommand
# 引入flask-script
from flask_script import Manager
# python中os模块获取环境变量的一个方法，FLASK_ ENV为flask中内置的配置变量
env = os.environ.get("FLASK_ ENV", "develop")
# env = os.environ.get("FLASK_ ENV", "testing")
# 创建一个app
app = create_app(env)
# 使用Manager实例调用script命令
manager = Manager(app)
# flask-migrate也支持flask-script的命令行接口，所以可以用flask-script统一管理，
# flask-migrate提供了一个ManagerCommand类，可以附加在flask-script的Manager类实例上
manager.add_command('db', MigrateCommand)
# flask的启动方法


from flask_apscheduler import APScheduler
from App.tools.sensorutl import sensorutl
from App.tools.camerautl import VideoCamera
from App.views.surveillance import record_status_without_json
abnormally = False
scheduler = APScheduler()

def check_sensor():
    with app.app_context():
        global abnormally
        TEMPERATURE_LIMIT = 28
        HUMIDITY_LIMIT = 60
        temperature = sensorutl.temperature()
        humidity = sensorutl.humidity()
        print(temperature, humidity)
        if temperature < TEMPERATURE_LIMIT and humidity < HUMIDITY_LIMIT and not abnormally:
            print(1)
            pass
        elif (temperature >= TEMPERATURE_LIMIT or humidity >= HUMIDITY_LIMIT) and not abnormally:
            print(2)
            record_status_without_json(status=True)
            abnormally = True
        elif temperature < TEMPERATURE_LIMIT and humidity < HUMIDITY_LIMIT and abnormally:
            print(3)
            record_status_without_json(status=False)
            abnormally = False
        elif (temperature >= TEMPERATURE_LIMIT or humidity >= HUMIDITY_LIMIT) and abnormally:
            print(4)
            pass


if __name__ == '__main__':
    manager.run()
