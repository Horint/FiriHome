from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from model import BlogAuthor, BlogComent

class PostAuthor(ModelForm):
    class Meta:
        model = BlogAuthor

class PostComent(ModelForm):
    class Meta:
        model = BlogComent