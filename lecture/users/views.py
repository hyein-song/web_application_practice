from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    # mdoel 처리가 있으면 model을 이용해서 데이터를 가져온다
    # 로직처리할것이 있으면 로직처리 진행
    # template 를 이용해서 결과를 만들어서 return
    return render(request, 'users/login.html', {
        'page_tile': 'User Login',
        'user_data': '소리없는 아우성'
    })


def signup(request):
    return render(request, 'users/signup.html', {
        'page_title': '회원가입'
    })


def signup_process(request):
    user_id = request.POST['inputId']
    u_pass1 = request.POST['inputPassword1']
    u_pass2 = request.POST['inputPassword2']

    # 사용자 ID는 unique해야 함
    user_list = User.objects.all()
    if user_list.filter(username=user_id).exists():
        return render(request, 'users/signup.html', {
            'err_msg': '존재하는 아이디 입니다.'
        })
    elif u_pass1 == u_pass2:
        # 회원가입 가능
        User.objects.create_user(username=user_id, password=u_pass1)
        return redirect('home')
    else:
        return render(request, 'users/signup.html', {
            'err_msg': '비밀번호가 달라요.'
        })


def login_process(request):
    u_id = request.POST['inputId']
    u_pw = request.POST['inputPassword']
    # DB에 해당 ID와 PW가 있는지 확인
    user = auth.authenticate(request, username=u_id, password=u_pw)
    if user is not None: # 로그인 됨
        # 로그인 처리를 진행(session 처리 진행)
        auth.login(request, user)
        user_dict = {
            'u_id': user.id,
            'u_name': user.username
        }
        # session 처리
        request.session['loginObj'] = user_dict
        return redirect('home')
    else:
        return render(request, 'users/login.html', {
            'err_msg': '로그인 실패입니다.'
        })


def logout(request):
    # session 정보 만료(삭제)
    auth.logout(request)
    return redirect('home')


