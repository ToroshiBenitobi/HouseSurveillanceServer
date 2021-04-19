from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
if False:
    from App.tools.sensorutl import sensorutl
else:
    from App.toolsvirtual.sensorutl import sensorutl
sensorblue = Blueprint('sensorblue', __name__)

@sensorblue.route('/sensor/temperatureinfo', methods=['POST', 'GET'])
def temperatureinfo():
    return str(sensorutl.temperature())

@sensorblue.route('/sensor/humidityinfo', methods=['POST', 'GET'])
def humidityinfo():
    return str(sensorutl.humidity())

