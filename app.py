from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
import wtforms


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        return "Form accept"


if __name__ == '__main__':
    print(dir(wtforms))
    app.run(port=8080, host='127.0.0.1')
