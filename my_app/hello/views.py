from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)


@hello.route('/')
@hello.route('/hello')
def hello_w():
    return MESSAGES['default']
