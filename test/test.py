# -*- coding: utf-8 -*-
from flask import Flask, render_template
from forms import LoginForm
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret'
               )
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Эльдар Рязанов'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         },
#         {
#             'author': {'username': 'Ипполит'},
#             'body': 'Какая гадость эта ваша заливная рыба!!'
#         }
#     ]
#     return render_template('test.html', title='Home', user=user, posts=posts)a

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sign In', form = form)

if __name__ == '__main__':
    app.run()