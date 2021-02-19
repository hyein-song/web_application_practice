from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect


def login(request):
    return render(request, 'users/login.html', {
        'page_title': 'User Login'
    })


def login_process(request):
    user_email = request.POST['userEmail']
    user_password = request.POST['userPassword']
    user = auth.authenticate(request, username=user_email, password=user_password)
    if user is not None:
        auth.login(request, user)
        user_dict = {
            'u_id': user.id,
            'u_name': user.username
        }
        request.session['loginObj'] = user_dict
        return redirect('home')
    else:
        return render(request, 'users/login.html', {
            'err_msg': '로그인 실패입니다. 다시 시도해보세요!'
        })


def signup(request):
    return render(request, 'users/signup.html', {
        'page_title': 'User Signup'
    })


def signup_process(request):
    u_email = request.POST['userEmail']
    u_password1 = request.POST['userPassword1']
    u_password2 = request.POST['userPassword2']

    # 이미 존재하는 id(이메일)인지를 확인
    user_list = User.objects.all()
    if user_list.filter(username=u_email).exists():
        return redirect('users:signup', {
            'err_msg': '존재하는 ID입니다.'
        })
    elif u_password1 == u_password2:
        user = User.objects.create_user(username=u_email, password=u_password1)
        auth.login(request, user)
        user_dict = {
            'u_id': user.id,
            'u_name': user.username
        }
        request.session['loginObj'] = user_dict
        return redirect('home')
    else:
        return render(request, 'users/signup.html', {
            'err_msg': '비밀번호가 일치하지 않습니다.'
        })


def logout(request):
    auth.logout(request)
    return redirect('home')
