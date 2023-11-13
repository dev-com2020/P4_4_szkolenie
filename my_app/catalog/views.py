from flask import Blueprint, jsonify, request
from my_app import db
from my_app.catalog.models import Product, Category

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/catalog')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product.id] = {
            'name': product.name,
            'price': str(product.price),
            'category': product.category.name
        }
    return jsonify(res)


@catalog.route('/product-create', methods=['POST'])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    categ_name = request.form.get('category')
    category = Category.query.filter_by(name=categ_name).first()
    if not category:
        category = Category(categ_name)

    product = Product(name, price, category)
    db.session.add(product)
    db.session.commit()
    return 'Product added'


@catalog.route('/category-create', methods=['POST'])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session(category)
    db.session.commit()
    return 'Kategoria dodana'


@catalog.route('/product/<id>')
def product(id):
    product = Product.query.get_or_404(id)
    return 'Produkt - %s, PLN %s' % (product.name, product.price)


@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    res = {}
    for c in categories:
        res[c.id] = {
            'name': c.name,
        }
        for product in c.products:
            res[c.id]['products'] = {
                'id': product.id,
                'name': product.name,
                'price': product.price
            }
    return jsonify(res)
