from flask import Flask, request, jsonify, render_template
import pandas as pd

app_1 = Flask(__name__)


@app_1.route('/api/users', methods=['GET', 'POST', 'DELETE'])
def users():
    if request.method == 'GET':
        df = pd.read_csv('users.csv')
        return {'users': df.to_dict()}, 200
    if request.method == 'POST':
        df = pd.read_csv('users.csv')
        data = request.get_json()
        user = [data['userid'], data['name'], data['bookid']]
        df = df.append(pd.Series(user, index=df.columns), ignore_index=True)
        df.to_csv('users.csv', index=False)
        return {'message': 'user added'}, 201
    if request.method == 'DELETE':
        df = pd.read_csv('users.csv')
        data = request.get_json()
        df = df[df.name != data['name']]
        df.to_csv('users.csv', index=False)
        return {'message': 'user deleted'}, 200


@app_1.route('/api/books', methods=['GET'])
def books():
    df = pd.read_csv('users.csv')
    data = request.get_json()
    user = data['user']
    bookid = df[df.name == user].bookid.values[0]
    booksdf = pd.read_csv('books.csv')
    book = booksdf[booksdf.bookid == bookid]
    if df[df.name == user].empty:
        return {'message': 'user not found'}, 404
    return {'book': book.to_dict()}, 200


@app_1.route('/table')
def show_tables():
    data = pd.read_csv('users.csv')
    data.set_index(['name'], inplace=True)
    data.index.name = None
    return render_template('view.html', tables=[data.to_html()], titles=['persons'])


if __name__ == '__main__':
    app_1.run(debug=True)
