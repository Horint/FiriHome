from flask import Flask, request
import random
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class AnswerForm(FlaskForm):
    answer = StringField(label='Answer', validators=[
        validators.Length(min=1, max=3)
    ])

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
    # MY_RANDOM_SEED=os.environ['FLASK_RANDOM_SEED']
)
random.seed(100)
random.randint(0, 100)
a = random.randint(0, 100)
r_answer = str(a)
# random.seed(app.config['MY_RANDOM_SEED'])

class AnswerForm(FlaskForm):
    answer = StringField(label='Answer', validators=[
        validators.Length(min=1, max=3)
    ])

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = AnswerForm(request.form)

        if form == r_answer:
            return ('=', 200)
        # elif form >= a:
        #     return (('>', 200))
        # elif form <= a:
        #     return (('<', 200))

    elif request.method == 'GET':
        return 'Число выбранно', 200

if __name__ == '__main__':
    app.run()

# # @app.route('/answer', methods=['POST', 'GET'])
# # def answe():
# #     if request.method == 'POST':
# #         print(request.form)
# #         form = ContactForm(request.form)
# #         print(form.va)
# #             return OTVET
# #     return OTVET
# app.run()
#
# # @app.route('/login', methods=['POST', 'GET'])
# # def login():
# #     error = None
# #     if request.method == 'POST':
# #         if valid_login(request.form['username'],
# #                        request.form['password']):
# #             return log_the_user_in(request.form['username'])
# #         else:
# #             error = 'Invalid username/password'
# #     # следущий код выполняется при методе запроса GET
# #     # или при признании полномочий недействительными
# #     return render_template('login.html', error=error)
# #
# # @app.route('/', methods=['GET', 'POST'])
# # def home():
# #     storage = Storage()
# #     all_items = storage.items
# #
# #     if request.method == 'POST':
# #         form = BlogPostForm(request.form)
# #         if form.validate():
# #             model = BlogPostModel(form.data)
# #             all_items.append(model)
# #         else:
# #             logger.error('Someone have submitted an incorrect form!')
# #     else:
# #         form = BlogPostForm()
#
# # import os
# # import random
# #
# # from flask import Flask
# # app = Flask(__name__)
# # app.config['RANDOM']=os.environ['FLASK_RANDOM_SEED']
#
# # random.seed(app.config['RANDOM'])
# #
# #
# # @app.route("/", methods=['GET'])
# # def hello():
# #     return os.environ['FLASK_RANDOM_SEED']
# #
# # @app.route("/random", methods=['GET'])
# # def my_random():
# #     return str(random.randint(1, 100))
# #
# #
# # app.run()
