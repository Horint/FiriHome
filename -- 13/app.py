from flask import Flask, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import fields, validators
# from wtforms_alchemy import ModelForm

app = Flask(__name__)
app.config.update(
    DEBUG=True,

    SQLALCHEMY_DATABASE_URI='sqlite:///book.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    WTF_CSRF_ENABLED=False
)

db = SQLAlchemy(app)
#
# class PostForm(ModelForm):
#     class Meta:
#         model = Text


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    time_of_writing = db.Column(db.DateTime, index=True, default= None)

    # def __str__(self):
    #     return("<GuestBook id - {}>".format(self.id))

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'text': self.text,
            'time_of_writing': self.time_of_writing,
        }


@app.route('/', methods =['GET'])
def index():
    book = GuestBookItem.query.all()
    return jsonify([b.to_dict() for b in book])

@app.route('/add', methods = ['POST'])
def my_add():
    print(request.form)
    my_author = request.form["author"]
    text = request.form["text"]
    # my_text = request.form["text"]

    # if form.validate():
    #     text_author_to_add = Text(**form.data)
    #     db.session.add(text_author_to_add)
    #     db.session.commit()
    my_post = GuestBookItem (author=my_author, text=text, time_of_writing=datetime.now()  )
    db.session.add(my_post), db.session.commit()
    # return db.session.add(my_post), db.session.commit()

if __name__ == '__main__':

    db.create_all()
    db.session.commit()

    # GuestBookItem.query.delete()

    # odin = GuestBookItem (author=my_author, text=my_text )
    # dva = GuestBookItem(author='Sveta', text='Privet Sveta')
    # tri = GuestBookItem(author='Semen', text='Privet Semen')
    # chet = GuestBookItem(author='Kolya', text='Privet Kolya')

    # # db.session.add(my_post)
    # db.session.commit(my_post)
    app.run()