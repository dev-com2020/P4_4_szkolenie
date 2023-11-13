# dla mac'a w terminalu przed uruchomieniem serwera
# export FLASK_APP=run.py
# set FLASK_APP=run.py
# python3 -m flask run
from my_app import app

if __name__ == '__main__':
    app.run()