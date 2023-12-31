from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import click
import pandas as pd

app2 = Flask(__name__)

app2.config["SECRET_KEY"] = 'N^Y&*8974r2w'
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app2)



class Data(db.Model):
    passId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, default=-1)

    def __init__(self, passId, name, age):
        self.passId = passId
        self.name = name
        self.age = age

    def __repr__(self):
        return str(self.passId) + ' -- ' + str(self.name) + ' -- ' + str(self.age)


@app2.cli.command("load-data")
@click.argument('fname')
def load_data(fname):
    print('*** Load from file: ' + fname)
    df = pd.read_csv(fname)
    for row in df.itertuples(index=False):
        print('********************')
        v_passId = row[0]
        v_name = row[3]
        v_age = row[5]
        print("PassId = " + str(v_passId))
        print("Name = " + str(v_name))
        print("Age = " + str(v_age))

        obj = Data(v_passId, v_name, v_age)
        db.session.add(obj)

    db.session.commit()


@app2.route('/')
def hello():
    retVal = 'Witaj, baza posiada (' + str(len(Data.query.all())) + ') wierszy'
    retVal += '<br/> zobacz dane <a href="/data">tutaj</a>'
    return retVal


@app2.route('/data')
def data():
    retVal = 'Rows = ' + str(len(Data.query.all())) + "<br/>"
    for row in Data.query.all():
        retVal += '<br/>' + str(row.__repr__())
    return retVal
