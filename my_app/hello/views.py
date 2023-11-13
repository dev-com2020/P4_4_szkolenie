from flask import Blueprint
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)

@hello.route('/hello')
def hello():
    return MESSAGES['default']
