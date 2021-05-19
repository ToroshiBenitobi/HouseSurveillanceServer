from App.ext import db
from datetime import datetime

# 用户数据模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    username = db.Column(db.String(100))  # 姓名【个人信息】【不可修改】

    password = db.Column(db.String(100))  # 密码

    number = db.Column(db.String(100))  # 学号【个人信息】【不可修改】
    phone = db.Column(db.String(100))  # 手机号【个人信息】gggg
    email = db.Column(db.String(100))  # 邮箱【个人信息】
    roomid = db.Column(db.Integer)
    roomname = db.Column(db.String(100))  # 寝室地址【个人信息】【不可修改】
    department = db.Column(db.String(100))  # 部门名称【个人信息】【不可修改】
    myclass = db.Column(db.String(100))  # 班级名称【个人信息】【不可修改】
    roommate1 = db.Column(db.String(100))  # 室友一【个人信息】【不可修改】
    roommate2 = db.Column(db.String(100))  # 室友二【个人信息】【不可修改】
    roommate3 = db.Column(db.String(100))  # 室友三【个人信息】【不可修改】

    # hzw
    roomidentity = db.Column(db.String(100))  # 寝室身份权限

    introduction = db.Column(db.String(100))  # 个人简介
    userpic = db.Column(db.String(100))  # 个人图片
    # qqt
    orders = db.relation('Order', backref='user')


# 智慧寝室部分
class Room(db.Model):
    roomid = db.Column(db.Integer, primary_key=True)  # 编号
    roomname = db.Column(db.String(100))  # 房间名
    roomadmin = db.Column(db.String(100))  # 宿管
    roomleader = db.Column(db.String(100))  # 寝室长
    # hzw
    currentnumber = db.Column(db.Integer)  # 当前人数

    intemperature = db.Column(db.String(100))  # 室内温度
    inhumidity = db.Column(db.String(100))  # 室内湿度
    outtemperature = db.Column(db.String(100))  # 室外温度
    outhumidity = db.Column(db.String(100))  # 室外湿度

    # hzw
    equipmentstatus = db.Column(db.String(100))  # 设备损坏情况
    suspecteddamage = db.Column(db.String(100))  # 可疑损坏设备
    reportinformation = db.Column(db.String(100))  # 上报信息
    cleancondition = db.Column(db.String(100))  # 寝室卫生
    safety = db.Column(db.String(100))  # 安全程度

    waterlave = db.Column(db.Integer)  # 剩余水费
    lightlave = db.Column(db.Integer)  # 剩余电费

    watermoney = db.Column(db.Integer)  # 水费
    lightmoney = db.Column(db.Integer)  # 电费


# qqt
# 账单信息
class Order(db.Model):
    orderid = db.Column(db.Integer, primary_key=True)  # 订单编号
    # id = db.Column(db.Integer)   #用户编号
    orderdate = db.Column(db.DateTime)  # 订单日期
    watercost = db.Column(db.Integer)  # 充值水费
    lightcost = db.Column(db.Integer)  # 充值电费
    id = db.Column(db.Integer, db.ForeignKey('user.id'))


# Video
class Video(db.Model):
    videoid = db.Column(db.Integer, primary_key=True)  # id of video
    savepath = db.Column(db.String(50))  # path where video saved
    videoname = db.Column(db.String(50))  # name of video
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))


# Message
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(255))
    datetime = db.Column(db.DateTime, default=datetime.now)
    text = db.Column(db.String(255))
