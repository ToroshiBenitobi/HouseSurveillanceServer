from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order

sensorblue = Blueprint('sensorblue', __name__)

@sensorblue.route('/sensor', methods=['POST', 'GET'])
def sensor():
    pass