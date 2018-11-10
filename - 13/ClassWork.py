from flask import Flask, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.update(
    DEBUG=True,

    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///book.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    WTF_CSRF_ENABLED=False
)

db = SQLAlchemy(app)


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(100), nullable=False)
    time_of_writing = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return("<GuestBook id - {}>".format(self.id))

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'text': self.text,
            'time_of_writing': self.time_of_writing,
        }


@app.route('/items', methods =['GET', 'POST'])
def index():
    book = GuestBookItem.query.all()
    return jsonify([b.to_dict() for b in book])

if __name__ == '__main__':
    db.create_all()

    # Deleting all records:
    GuestBookItem.query.delete()

    # Creating new ones:
    odin = GuestBookItem (author='Ivan', text='Privet Ivan' )
    dva = GuestBookItem(author='Sveta', text='Privet Sveta')
    tri = GuestBookItem(author='Semen', text='Privet Semen')
    chet = GuestBookItem(author='Kolya', text='Privet Kolya')

    db.session.add(odin)
    db.session.add(dva)
    db.session.add(tri)
    db.session.add(chet)
    db.session.commit()

    # Running app:

    app.run()