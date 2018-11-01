# # -*- coding: utf-8 -*-
# import time
# import requests
# r = requests.get('https://www.reddit.com/r/Python/comments/9q6xtx/things_i_wish_python_did_differently/')
# time.sleep(10)
# with open ('test.html', 'w', encoding='utf-8')
#         # as out_put:
#     # time.sleep(10)
#     out_put.write(r.text)
# print(r.text)
#
#
# # <!-- END TEMPLATE: bbcode_quote --> Место начала сообщения
# # <!-- message -->


from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # удалить из сессии имя пользователя, если оно там есть
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.run()