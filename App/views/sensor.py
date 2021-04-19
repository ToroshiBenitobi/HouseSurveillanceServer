from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
from App.tools.sensor import sensor
sensorblue = Blueprint('sensorblue', __name__)

@sensorblue.route('/sensor/temperatureinfo', methods=['POST', 'GET'])
def temperatureinfo():
    return sensor.temperature_value