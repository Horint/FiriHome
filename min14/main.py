
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

@app.route('/', methods =['GET'])
def index():
    from model import BlogAuthor, BlogComent
    myblog = BlogAuthor.query.all()
    mycom = BlogComent.query.all()
    return jsonify([b.to_dict() for b in myblog]), jsonify([a.to_dict() for a in mycom])

# @app.route('/coment', methods =['GET'])
# def index_coment():
#     blog = BlogComent.query.all()
#     return jsonify([a.to_dict() for a in blog])

@app.route('/add/author', methods=['POST'])
def my_add():
    from form import BlogForm
    from model import BlogAuthor
    form = BlogForm(request.form)
    if form.validate():
        my_post = BlogAuthor(**form.data)
        db.session.add(my_post)
        db.session.commit()
    return

@app.route('/add/comment', methods=['POST'])
def my_add_post():
    from model import BlogAuthor, BlogComent
    from form import ComentForm, BlogForm
    form = ComentForm(request.form)
    if form.validate():
        my_post = BlogComent(**form.data)
        db.session.add(my_post)
        db.session.commit()
    return

if __name__ == '__main__':
    # from model import BlogAuthor, BlogComent
    # from form import ComentForm, BlogForm
    db.create_all()
    db.session.commit()
    app.run()

