from django.shortcuts import render, redirect, get_object_or_404
from bbs.models import Post
from bbs.forms import PostForm

# Create your views here.


def p_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'bbs/list.html', {'posts': posts})


def p_create(request):

    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('bbs:p_list')

    if request.method == 'GET':
        post_form = PostForm()
        return render(request, 'bbs/create.html', {'post_form': post_form})


# def p_modify(request):
#     post_form = PostForm(Post.author, Post.contents)
#     return render(request, 'bbs/modify.html', {'post_form': post_form})

def p_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post_form.save()
            return redirect('bbs:p_list', post_id=post.pk)

    if request.method == 'GET':
        post_form = PostForm(instance = post)
        return render(request, 'bbs/modify.html', {'post_form': post_form})
