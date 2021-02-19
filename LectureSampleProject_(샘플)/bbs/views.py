from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from datetime import datetime
from django.core.paginator import Paginator


def p_list(request):
    # 데이터베이스의 모든 글의 내용을 다 들고와야 해요!
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    bbs_page = paginator.get_page(page)

    return render(request, 'bbs/list.html', {
        'post_list': posts,
        'bbs_page': bbs_page
    })


def p_create(request):
    # POST방식
    if request.method == 'POST':
        # 데이터베이스에 저장!!
        # 사용자가 전달해준 데이터는 request.POST 안에 들어있어요!
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            obj = post_form.save(commit=False)
            user = User.objects.get(username=request.user.username)
            obj.author = user
            obj.author_name = request.user.username
            obj.p_date = datetime.now()
            obj.save()
            return redirect('bbs:p_list')
        else:
            print('먼가이상해요!!')
            return redirect('bbs:p_list')


    # GET방식
    if request.method == 'GET':
        # 빈입력 form을 출력하는 코드가 나오면 되요!
        post_form = PostForm()
        return render(request, 'bbs/create.html',
                      {'post_form': post_form})


def p_detail(request, post_id):
    # 조회수를 올린다
    post = Post.objects.get(pk=post_id)
    post.p_count += 1
    post.save()

    return render(request, 'bbs/detail.html', {
        'post': post
    })


def p_delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect('bbs:p_list')


def p_update(request, post_id):
    post = Post.objects.get(pk=post_id)

    # post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.p_date = datetime.now()
            obj.save()
            return redirect('bbs:p_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'bbs/update.html', {
        'post_form': form
    })
