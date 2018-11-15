from flask import Flask, jsonify, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config.update(
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI='sqlite:///blog.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    WTF_CSRF_ENABLED=False
)

db = SQLAlchemy(app)
db.create_all()

from dz14.model import BlogAuthor, BlogComent
from dz14.forms import PostAuthor, PostComent
# class BlogAuthor(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     text = db.Column(db.String(1000), nullable=False)
#     # time_of_writing = db.Column(db.DateTime, index=True, default= datetime.now)
#     coment = db.relationship('BlogComent', backref = 'coments', lazy = 'dynamic')
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
#     coment_to_blog = db.Column(db.String(1000), db.ForeignKey('blogauthor'.text), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('blogauthor'.text))
#
#     def to_dict(self):
#         return {
#             'id': self.id,
#             'coment_to_blog': self.title,
#             # 'text': self.text,
#             # 'time_of_writing': self.time_of_writing,
@app.route('/', methods =['GET'])
def index():
    blog = BlogAuthor.query.all()
    return jsonify([b.to_dict() for b in blog])

@app.route('/coment', methods =['GET'])
def index_coment():
    blog = BlogComent.query.all()
    return jsonify([a.to_dict() for a in blog])

@app.route('/add/author', methods=['POST'])
def my_add():
    form = BlogForm(request.form)
    if form.validate():
        my_post = BlogAuthor(**form.data)
        db.session.add(my_post)
        db.session.commit()
    return

@app.route('/add/comment', methods=['POST'])
def my_add_post():
    form = PostComent(request.form)
    if form.validate():
        my_post = ComentForm(**form.data)
        db.session.add(my_post)
        db.session.commit()
    return

if __name__ == '__main__':

    # db.create_all()
    db.session.commit()
    app.run()


