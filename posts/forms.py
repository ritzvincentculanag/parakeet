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
                    'class': 'form__post-content',
                    'placeholder': 'What\'s chirping?',
                    'maxlength': 250,
                    'rows': 5,
                }
            ),
            'status': Select(
                attrs={
                    'class': 'form__post-status'
                }
            )
        }
