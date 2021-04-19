from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response
from App.models import db, Order

camerablue = Blueprint('camerablue', __name__)

@camerablue.route('/camera', methods=['POST', 'GET'])
def camera():
    return 'camera'