from django.shortcuts import render

from posts.models import Post


def post_list(request):
    posts = Post.published.all()

    return render(
        request=request,
        template_name='posts/list.html',
        context={ 'posts': posts }
    )
