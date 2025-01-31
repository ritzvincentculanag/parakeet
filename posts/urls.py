from django.urls import path

from posts.views import *

app_name = "posts"

urlpatterns = [
    path(
        route='',
        view=post_list,
        name='post_list'
    )
]
