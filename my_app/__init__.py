from flask import Flask
from my_app.hello.views import hello

app = Flask(__name__)
app.config.from_pyfile('setup.cfg')
# app.config.from_object('config.ProductionConfig')
app.register_blueprint(hello)