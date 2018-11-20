from main import db

class BlogAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(1000), nullable=False)

class BlogComent(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True )
    coment_to_blog = db.Column(db.String(1000))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogauthor.id'))





# class BlogAuthor(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.String(1000), nullable=False)
#     # time_of_writing = db.Colum2n(db.DateTime, index=True, default= datetime.now)
#     coment_id = db.Column(db.Integer, db.ForeignKey('blogcoment.id'))
#     coment = db.relationship('BlogComent', backref='comentssss')
#
#     # db.relationship("BlogComent") #, backref = 'COMENTS')
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
#         }
#
# class BlogComent(db.Model):
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True )
#     coment_to_blog = db.Column(db.String(1000))
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'coment_to_blog': self.coment_to_blog,
#             'blog_id': self.blog_id,
#             # 'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
#         }


# class BlogAuthor(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.String(1000), nullable=False)
#     # time_of_writing = db.Colum2n(db.DateTime, index=True, default= datetime.now)
#     coment = db.relationship("BlogComent")
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
#         }
#
# class BlogComent(db.Model):
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True )
#     coment_to_blog = db.Column(db.String(1000))
#     blog_id = db.Column(db.Integer, db.ForeignKey('blogauthor.id'))
#     blog = db.relationship("BlogAuthor", back_populates="COMENTSSSSS")
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'coment_to_blog': self.title,
#             # 'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
#         }

# class BlogAuthor(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.String(1000), nullable=False)
#     # time_of_writing = db.Colum2n(db.DateTime, index=True, default= datetime.now)
#     coment = db.relationship("BlogComent") #, backref = 'COMENTS')
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
#         }
#
# class BlogComent(db.Model):
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True )
#     coment_to_blog = db.Column(db.String(1000))
#     blog_id = db.Column(db.Integer, db.ForeignKey('blogauthor.id'))
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'coment_to_blog': self.coment_to_blog,
#             'blog_id': self.blog_id,
#             # 'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
#         }