from flask import Blueprint

from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)


@hello.route('/')
@hello.route('/hello')
def hello_w():
    return "Test"

@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or f"{key} nie znaleziony!"

