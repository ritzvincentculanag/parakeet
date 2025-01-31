from django.shortcuts import redirect, render
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post


def post_list(request):
    form = PostForm()
    posts = Post.published.all()

    return render(
        request=request,
        template_name='posts/list.html',
        context={ 
            'posts': posts,
            'form': form 
        }
    )

def post_create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

        return redirect(reverse('posts:post_list'))
    
    return render(
        request=request,
        template_name='posts/list.html',
        context= { 'form': form }
    )
