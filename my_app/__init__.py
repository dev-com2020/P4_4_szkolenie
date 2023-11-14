import os.path

from flask import Flask, request, typing as ft
from flask.views import View
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from my_app.hello.views import hello
from my_app.product.views import product_blueprint
import ccy


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.secret_key = "cn743289e"
app.config["WTF_CSRF_SECRET_KEY"] = "nc7634$#"
app.config.from_pyfile('setup.cfg')
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/images'
# app.config.from_object('config.ProductionConfig')
# app.register_blueprint(hello)
# app.register_blueprint(product_blueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/baza'

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)


@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:] or 'USD')
    return '{0} {1}'.format(currency_code, amount)


class GetPostRequest(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'GET':
            bar = request.args.get('foo', 'bar')
        else:
            bar = request.form.get('foo', 'bar')
        return 'Simple request where foo is %s' % bar


app.add_url_rule('/req2', view_func=GetPostRequest.as_view('req2'))

from my_app.catalog.views import catalog, ProductView

product_view = ProductView.as_view('product_view')
app.add_url_rule('/api/', view_func=product_view, methods=['GET', 'POST'])
app.add_url_rule('/api/<int:id>', view_func=product_view, methods=['GET', 'PUT', 'DELETE'])
app.register_blueprint(catalog)

with app.app_context():
    db.create_all()
