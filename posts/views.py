from django.shortcuts import redirect, render
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post, Like


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
        context={'form': form}
    )


def post_like(request, post_id):
    author = request.user
    post = Post.objects.get(id=post_id)
    like = Like.objects.filter(post=post, author=author)

    if like.exists():
        like.delete()
    else:
        like = Like.objects.create(post=post, author=author)
        like.save()

    return redirect(reverse('posts:post_list'))
