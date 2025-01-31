from django.forms import *

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content','status']
        widgets = { 
            'content': Textarea(
                attrs={
                    'cols': 80,
                    'rows': 10
                }
            )
        }
