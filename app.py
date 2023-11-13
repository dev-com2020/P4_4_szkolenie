from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('setup.cfg')

@app.route('/')
def hello_world():
    return 'Witaj Flasku...'


if __name__ == '__main__':
    app.run()


# dla mac'a w terminalu przed uruchomieniem serwera
# export FLASK_APP=app.py
# python3 -m flask run