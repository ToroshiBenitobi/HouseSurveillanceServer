from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order
from App.tools.sensorutl import sensorutl
sensorblue = Blueprint('sensorblue', __name__)
@sensorblue.route('/sensor/temperatureinfo', methods=['POST', 'GET'])
def temperatureinfo():
    return str(sensorutl.temperature)
