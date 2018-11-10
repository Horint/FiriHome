from datetime import date

from sqlalchemy_example.app import db

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