from flask import Flask
from my_app.hello.views import hello
from my_app.product.views import product_blueprint

app = Flask(__name__)
app.config.from_pyfile('setup.cfg')
# app.config.from_object('config.ProductionConfig')
app.register_blueprint(hello)
app.register_blueprint(product_blueprint)