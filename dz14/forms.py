from wtforms_alchemy import ModelForm

from dz14.model import BlogAuthor, BlogComent

class BlogForm(ModelForm):
    class Meta:
        model = BlogAuthor

class ComentForm(ModelForm):
    class Meta:
        model = BlogComent