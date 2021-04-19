# Python中的日期类型引入
from datetime import timedelta
from datetime import datetime
# 引入Flask
from flask import Flask
# 引入扩展模块
from App.ext import init_ext
# 引入配置模块
from App.settings import envs
# from App.myconfig import envs
# 引入蓝图模块，有多少引入多少
from App.views.user import userblue
from App.views.room import roomblue
from App.views.camera import camerablue
from App.views.sensor import sensorblue
from App.views.order import orderblue


def create_app(env):
    # 创建app,由主入口manage.py进行调用create_app
    app = Flask(__name__)

    # 通过setting.py初始化此app
    # app.config.from_object(envs.get(env))
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/housebrainlite'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    app.config.from_object(envs.get(env))

    # 注册蓝图
    app.register_blueprint(userblue)
    app.register_blueprint(roomblue)
    app.register_blueprint(orderblue)
    app.register_blueprint(camerablue)
    app.register_blueprint(sensorblue)

    # 初始化第三方扩展库，包括SQLAlchemy及Migrate等第三方库
    init_ext(app=app)

    # 配置Flask-WTF，即设置session，通过加密或签名以不同的方式提升安全性
    app.config['SECRET_KEY'] = 'housebrain will change the world'
    # 设置session的保存时间
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

    return app
