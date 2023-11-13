from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort

from my_app.product.models import PRODUCTS

product_blueprint = Blueprint('product', __name__)


@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS)


@product_blueprint.route('/product/<key>')
def product(key):
    prod = PRODUCTS.get(key)
    if not prod:
        abort(404)
    return render_template('product.html', product=prod)
