from flask import Blueprint, jsonify, request, render_template
from my_app import db
from my_app.catalog.models import Product, Category

catalog = Blueprint('catalog', __name__)


@catalog.route('/')
@catalog.route('/home')
def home():
    return render_template('home.html')


@catalog.route('/catalog')
@catalog.route('/catalog/<int:page>')
def products(page=1):
    products = Product.query.paginate(page=page, per_page=10)
    return render_template('products.html', products=products)

@catalog.route('/category/<id>')
def category(id):
    category = Category.query.get_or_404(id)
    return render_template('category.html', category=category)


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
    return render_template('product.html', product=product)


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
