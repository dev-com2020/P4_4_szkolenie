from functools import wraps

from flask import Blueprint, jsonify, request, render_template, flash, redirect, url_for
from my_app import db, app
from my_app.catalog.models import Product, Category

catalog = Blueprint('catalog', __name__)


def template_or_json(template=None):
    def decorated(f):
        @wraps(f)
        def decorated_fn(*args, **kwargs):
            ctx = f(*args, **kwargs)
            if request.headers.get("X-Requested-With") == "XMLHttpRequest" or not template:
                return jsonify(ctx)
            else:
                return render_template(template, **ctx)

        return decorated_fn

    return decorated


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@catalog.route('/')
@catalog.route('/home')
@template_or_json('home.html')
def home():
    products = Product.query.all()
    return {'ilość': len(products)}


@catalog.route('/catalog')
@catalog.route('/catalog/<int:page>')
def products(page=1):
    products = Product.query.paginate(page=page, per_page=10)
    return render_template('products.html', products=products)


@catalog.route('/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)


@catalog.route('/product-create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        categ_name = request.form.get('category')
        category = Category.query.filter_by(name=categ_name).first()
        if not category:
            category = Category(categ_name)

        product = Product(name, price, category)
        db.session.add(product)
        db.session.commit()
        flash('Produkt %s został dodany' % name, 'success')
        return redirect(
            url_for('catalog.product', id=product.id))
    return render_template('product-create.html')


@catalog.route('/category-create', methods=['POST'])
def create_category():
    name = request.form.get('name')
    category = Category(name)
    db.session(category)
    db.session.commit()
    return render_template('category.html', category=category)


@catalog.route('/product/<id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)


@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)


@catalog.route('/req', methods=['GET', 'POST'])
def some_req():
    if request.method == 'GET':
        bar = request.args.get('foo', 'bar')
    else:
        bar = request.form.get('foo', 'bar')
    return 'Simple request where foo is %s' % bar


@catalog.route('/test/<string(minlength=2, maxlength=3):code>')
def get_name(code):
    return code


@catalog.route('/test2/<int(min=18,max=99):age>')
def get_age(age):
    return str(age)
