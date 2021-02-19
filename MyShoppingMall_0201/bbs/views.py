from django.shortcuts import render, redirect
from bbs.models import Post
from bbs.forms import PostForm


def p_list(request):
    # DB의 모든 글의 내용을 다 들고와야 함
    posts = Post.objects.all().order_by('-id')
    return render(request, 'bbs/list.html', {'posts': posts})


def p_create(request):
    
    # POST 방식
    if request.method == 'POST':
        # DB에 저장
        # 사용자가 전달해준 데이터는 request.POST안에 들어있음
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('bbs:p_list')
        

    # GET 방식
    if request.method == 'GET':
        # 빈 입력 폼을 출력함
        post_form = PostForm()
        return render(request, 'bbs/create.html', {'post_form': post_form})
    
    
    
    
    