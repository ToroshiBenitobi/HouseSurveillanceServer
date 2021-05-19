"""API for JS Webapp Wall application.

In real life, for us to share messages between different users of this
application, we'd want to store the messages in a server-side persistent
store (like a relational database). However, since we're demonstrating how
to use client-side session systems, this stores things there.
"""
from flask import session
from html.parser import HTMLParser
from App.models import db, Message
from datetime import datetime

# So that you can play with the `get` API, we return a single
# test message as the default.

DEFAULT_MESSAGES = [
    {'message': '请留言'},
]


def wall_error(error):
    """Handle API errors.

        error: (string) error message

        returns: dictionary error object.
    """

    return {
        "result": error,
    }


def wall_list():
    """Get messages.

        returns: dictionary with messages list + result code.
    """
    messages = Message.query.all()
    messages_json = to_json_list(messages)
    print(messages)
    return {
        "result": "OK",
        "messages": messages_json,
    }


def wall_last():
    """ Return a dictionary with the result code and the last message submitted."""
    Message.query.first()
    return session["wall"][-1]["message"]


def wall_add(msg, user):
    """Set a new message.

        msg: (string) message

        returns: dictionary with messages list + result code.
    """

    parser = RemoveHTML()
    parser.feed(msg)
    msg = parser.out

    wall_dict = {
        "message": msg,
    }

    # session.setdefault('wall', []).append(wall_dict)
    message = Message()
    message.id = message.query.count() + 1
    # message.datetime = datetime.now
    message.user = user
    message.text = msg

    db.session.add(message)
    db.session.commit()

    result = {"result": "已发送消息", "messages": msg}

    return result


def wall_clear():
    db.session.delete(Message.query.all())
    result = {"result": "已清除消息板"}
    return result


class RemoveHTML(HTMLParser):
    out = ""

    def handle_data(self, data):
        self.out = self.out + data


def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object. """
    json = {}
    # json['fields'] = {}
    # json['pk'] = getattr(model, 'id')
    for col in model._sa_class_manager.mapper.mapped_table.columns:
        # json['fields'][col.name] = getattr(model, col.name)
        json[col.name] = str(getattr(model, col.name))

    # return dumps([json])
    return json


def to_json_list(model_list):
    json_list = []
    for model in model_list:
        json_list.append(to_json(model))
    return json_list