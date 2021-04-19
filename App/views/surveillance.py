from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order

surveillanceblue = Blueprint('surveillanceblue', __name__)

@surveillanceblue.route('/camera', methods=['POST', 'GET'])
def camera():
    return 'camera'