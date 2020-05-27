import requests
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/groceries')
def groceries():
    _json = json.loads(requests.get('http://0.0.0.0:5000/groceries').text)
    return render_template(
        'groceries/groceries.html', groceries=_json['groceries']
    )


@app.route('/groceries/add', methods=['GET', 'POST'])
def groceries_add():
    if request.method == 'GET':
        return render_template('groceries/manage.html')

    if request.method == 'POST':
        _request = requests.post('http://0.0.0.0:5000/grocery', json={
            'name': request.form['name'],
            'exp_date': request.form['exp_date']
        })
        print(_request.status_code)
        if _request.status_code == 200:
            return redirect(url_for('groceries'))
        return render_template('groceries/manage.html', response=json.loads(_request.text)['response'])


@app.route('/groceries/delete/<int:db_id>')
def groceries_delete(db_id):
    _request = requests.delete('http://0.0.0.0:5000/grocery', json={'id': db_id})
    return redirect(url_for('groceries'))


@app.route('/groceries/update/<int:db_id>', methods=['GET', 'POST'])
def groceries_update(db_id):
    if request.method == 'GET':
        _json = json.loads(
            requests.get('http://0.0.0.0:5000/grocery', json={'id': db_id}).text
        )
        return render_template('groceries/manage.html', grocery=_json)

    if request.method == 'POST':
        _request = requests.put('http://0.0.0.0:5000/grocery', json={
            'id': request.form['id'],
            'name': request.form['name'],
            'exp_date': request.form['exp_date']
        })
        return redirect(url_for('groceries'))


if __name__ == '__main__':
    app.run()
