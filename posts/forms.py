from django.forms import *

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content','status']
        labels = { 
            'content': '',
            'status': '',
        }
        widgets = { 
            'content': Textarea(
                attrs={
                    'class': 'post-create__content',
                    'placeholder': 'What\'s chirping?',
                    'rows': 5,
                }
            )
        }
