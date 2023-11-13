from flask import Flask, request
from my_app.hello.views import hello
from my_app.product.views import product_blueprint
import ccy

app = Flask(__name__)
app.config.from_pyfile('setup.cfg')
# app.config.from_object('config.ProductionConfig')
app.register_blueprint(hello)
app.register_blueprint(product_blueprint)


@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:] or 'USD')
    return '{0} {1}'.format(currency_code, amount)
