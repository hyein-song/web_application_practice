from django.shortcuts import render, redirect
from .models import Member
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    return render(request, 'users/login.html')


def login_process(request):
    u_id = request.POST['inputID']
    u_pass = request.POST['inputPassword']
    user = auth.authenticate(request, username=u_id, password=u_pass)

    if user is not None:
        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'users/login.html', {
            'err_msg': '로그인 실패입니다. 다시 시도해보세요!'
        })




def signup(request):
    return render(request, 'users/signup.html')


def signup_process(request):
    u_id = request.POST['inputID']
    u_pass1 = request.POST['inputPassword1']
    u_pass2 = request.POST['inputPassword2']
    u_tel = request.POST['inputTel']

    # 이미 존재하는 id(이메일)인지를 확인
    user_list = User.objects.all()
    if user_list.filter(username=u_id).exists():
        return render(request, 'users/signup.html', {
            'err_msg': '존재하는 ID입니다.'
        })
    elif u_pass1 == u_pass2:
        user = User.objects.create_user(username=u_id,
                                        password=u_pass1)
        member = Member(user=user, mobile=u_tel)
        member.save()

        auth.login(request, user)
        return redirect('home')
    else:
        return render(request, 'users/signup.html', {
            'err_msg': '비밀번호가 일치하지 않습니다.'
        })


def logout(request):
    auth.logout(request)
    return redirect('home')
