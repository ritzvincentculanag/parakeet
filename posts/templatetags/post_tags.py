from django import template
from posts.models import Like

register = template.Library()

@register.filter(name='post_liked')
def post_liked(post, user):
    return Like.objects.filter(post=post, author=user)
