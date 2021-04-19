from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
print('before import')
from App.tools.sensorutl import sensorutl
sensorblue = Blueprint('sensorblue', __name__)
print('after sensorblue')

@sensorblue.route('/sensor/temperatureinfo', methods=['POST', 'GET'])
def temperatureinfo():
    return str(sensorutl.temperature())

@sensorblue.route('/sensor/humidityinfo', methods=['POST', 'GET'])
def humidityinfo():
    return str(sensorutl.humidity())

