from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from my_app.hello.views import hello
from my_app.product.views import product_blueprint
import ccy

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app

app = Flask(__name__)

app.secret_key = "cn743289e"
app.config.from_pyfile('setup.cfg')
# app.config.from_object('config.ProductionConfig')
app.register_blueprint(hello)
app.register_blueprint(product_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/baza'

db = SQLAlchemy()
db.init_app(app)

@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:] or 'USD')
    return '{0} {1}'.format(currency_code, amount)

with app.app_context():
    db.create_all()