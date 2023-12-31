import json
import os.path
from functools import wraps

from flask import Blueprint, jsonify, request, render_template, flash, redirect, url_for, abort
from flask.views import MethodView
from flask_restful import Resource
from sqlalchemy.orm import join
from werkzeug.utils import secure_filename

from my_app import db, app, ALLOWED_EXTENSIONS
from my_app.catalog.models import Product, Category, ProductForm, CategoryForm

catalog = Blueprint('catalog', __name__)


class ProductView(MethodView):
    def get(self, id=None, page=1):
        if not id:
            products = Product.query.paginate(page=page, per_page=10).items
        else:
            products = [Product.query.get(id)]
        if not products:
            abort(404)
        res = {}
        for product in products:
            res[product.id] = {
                'name': product.name,
                'price': product.price,
                'category': product.category.name,
            }
        return json.dumps(res)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


def allowed_file(filename):
    return '.' in filename and filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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
    form = ProductForm(meta={'csrf': True})
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        category = Category.query.get_or_404(form.category.data)
        image = form.image.data
        if allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        product = Product(name, price, category, filename)
        db.session.add(product)
        db.session.commit()
        flash('Produkt %s został dodany' % name, 'success')
        return redirect(
            url_for('catalog.product', id=product.id))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('product-create.html', form=form)


@catalog.route('/category-create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm(meta={'csrf': False})
    if form.validate_on_submit():
        name = form.name.data
        category = Category(name)
        db.session.add(category)
        db.session.commit()
        flash('Kategoria %s została dodana' % name, 'success')
        return redirect(
            url_for('catalog.product', id=category.id))
    if form.errors:
        flash(form.errors, 'danger')
    return render_template('category-create.html', form=form)


@catalog.route('/product/<id>')
def product(id):
    product = Product.query.get_or_404(id)
    return render_template('product.html', product=product)


@catalog.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('categories.html', categories=categories)


@catalog.route('/product-search')
@catalog.route('/product-search/<int:page>')
def product_search(page=1):
    name = request.args.get('name')
    price = request.args.get('price')
    company = request.args.get('company')
    category = request.args.get('category')
    products = Product.query
    if name:
        products = products.filter(Product.name.like('%' + name + '%'))
    if price:
        products = products.filter(Product.price == price)
    if company:
        products = products.filter(Product.company.like('%' + company + '%'))
    if category:
        products = products.select_from(join(Product, Category)).filter(Category.name.like('%' + category + '%'))

    return render_template('products.html', products=products.paginate(page, 10))


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


class ProductApi(Resource):
    def get(self, id=None):
        return 'To jest get z api'

    def post(self):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

