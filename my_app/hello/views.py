from flask import Blueprint, render_template, request

from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)


@hello.route('/')
@hello.route('/hello')
def hello_w():
    mess = request.args.get('mess', MESSAGES)
    return render_template('index.html', mess=mess)


@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or f"{key} nie znaleziony!"


@hello.route('/add/<key>/<message>')
def add_or_update(key, message):
    MESSAGES[key] = message
    return f"{key} został dodany/zaktualizowany"
