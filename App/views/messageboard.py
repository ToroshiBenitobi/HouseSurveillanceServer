# qqt
from flask import Flask, Blueprint, render_template, session, redirect, url_for, request, Response, make_response
from App.models import db, Order
import json
from App.tools.messageutl import wall_list, wall_add, wall_error, wall_clear, wall_last

boardblue = Blueprint('boardblue', __name__)


@boardblue.route("/message", methods=['POST', 'GET'])
def message_board():
    """Return index page."""
    return render_template("smartroom/messageboard.html")


def _convert_to_JSON(result):
    """Convert result object to a JSON web request."""

    # In order for us to return a response that isn't just HTML, we turn our
    # response dictionary into a string-representation (using json.dumps),
    # then use the flask `make_response` function to create a response object
    # out of this.
    response = make_response(json.dumps(result))

    # We can then set some headers on this response object:

    # Access-Control-Allow-Origin isn't needed for this example, but it's
    # a demonstration of a useful feature: since it should be safe to allow
    # Javascript from websites other than ours to get/post to our API, we
    # explicitly allow this.
    response.headers['Access-Control-Allow-Origin'] = "*"

    # Setting the MIMETYPE to JSON's will explicitly mark this as JSON;
    # this can help some client applications understand what they get back.
    response.mimetype = "application/json"
    return response


@boardblue.route("/message/wall/list")
def list_messages():
    """Return list of wall messages as JSON."""

    result = wall_list()
    return _convert_to_JSON(result)


@boardblue.route("/message/wall/last")
def last_message():
    result = wall_last()
    return _convert_to_JSON(result)


@boardblue.route("/message/wall/add", methods=['POST'])
def add_message():
    """Add a message and return list of wall messages as JSON."""

    # Get the message from the "m" argument passed in the POST.
    # (to get things from a GET response, we've used request.args.get();
    # this is the equivalent for getting things from a POST response)
    msg = request.form.get('m').strip()

    if msg is None:
        result = wall_error("You did not specify a message to set.")

    elif msg == "":
        result = wall_error("Your message is empty")

    else:
        result = wall_add(msg)

    return _convert_to_JSON(result)


@boardblue.route('/message/wall/clear')
def clear_wall():
    """Clear all messages on wall and reset to the default message."""

    result = wall_clear()
    return _convert_to_JSON(result)
