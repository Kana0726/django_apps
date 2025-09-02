from django.forms import ModelForm
from .views import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text']
