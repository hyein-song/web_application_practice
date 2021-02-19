from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from datetime import datetime
from django.contrib.auth.models import User


def p_list(request):
    # 데이터베이스의 모든 글의 내용을 다 들고와야 해요!
    posts = Post.objects.all().order_by('-id')
    return render(request, 'bbs/list.html', {'post_list': posts})


def p_create(request):
    # POST방식
    if request.method == 'POST':
        # 데이터베이스에 저장!!
        # 사용자가 전달해준 데이터는 request.POST 안에 들어있어요!
        post_form = PostForm(request.POST)
        print(post_form)

        if post_form.is_valid():
            obj = post_form.save(commit=False)
            user = User.objects.get(username=request.session['loginObj']['u_name'])
            obj.author = user
            obj.author_name = request.session['loginObj']['u_name']
            obj.p_date = datetime.now()
            obj.save()
            return redirect('bbs:p_list')
        else:
            print('먼가이상해요!!')
            return redirect('bbs:p_list')
            # post_form.save()


    # GET방식
    if request.method == 'GET':
        # 빈입력 form을 출력하는 코드가 나오면 되요!
        post_form = PostForm()
        return render(request, 'bbs/create.html',
                      {'post_form': post_form})
