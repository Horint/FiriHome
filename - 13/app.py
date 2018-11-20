from flask import Flask, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms_alchemy import ModelForm

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///book.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    WTF_CSRF_ENABLED=False
)

db = SQLAlchemy(app)

class GuestBookItem(db.Mwwodel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    time_of_writing = db.Column(db.DateTime, index=True, default= datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'text': self.text,
            'time_of_writing': self.time_of_writing,
        }

class PostForm(ModelForm):
    class Meta:
        model = GuestBookItem

@app.route('/', methods =['GET'])
def index():
    book = GuestBookItem.query.all()
    return jsonify([b.to_dict() for b in book])


@app.route('/add', methods=['POST'])
def my_add():
    form = PostForm(request.form)

    if form.validate():
        my_post = GuestBookItem(**form.data)
        db.session.add(my_post)
        db.session.commit()

    return


if __name__ == '__main__':

    db.create_all()
    db.session.commit()
    app.run()