from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from model import BlogAuthor, BlogComent

class BlogForm(ModelForm):
    class Meta:
        model = BlogAuthor

class ComentForm(BlogAuthor):
    class Meta:
        model = BlogComent