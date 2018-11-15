from dz14.app import db

class BlogAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(1000), nullable=False)
    # time_of_writing = db.Column(db.DateTime, index=True, default= datetime.now)
    coments = db.relationship('BlogComent', backref = 'coment', lazy = 'dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            # 'time_of_writing': self.time_of_writing,
        }

class BlogComent(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    coment_to_blog = db.Column(db.String(1000), db.ForeignKey('blogauthor.id'), nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'coment_to_blog': self.title,
            # 'text': self.text,
            # 'time_of_writing': self.time_of_writing,
        }
