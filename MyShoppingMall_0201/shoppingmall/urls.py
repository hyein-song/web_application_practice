"""shoppingmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView # 내가 원하는 template을 바로 결과로 보여줌(view 로직 타지않고)

# url pattern설정할 때 사용할 수 있는 함수
# url(), path(), re_path()
# url() : 원조. 정규표현식을 포함해서 일반적인 설정이 가능
# path() : 일반문자열 형태로 url conf할때
# re_path() : 정규 표현식으로 url conf 할때
# 정규표현식 => [adh] => a,d,h 중에 하나(대괄호)
# [a-z] => a~z중 영문자 소문자 1개
# [a-z]{3} => 영분자 소문자 3개 (att)
# ^(Caret) : 문자열의 시작, $ :  문자열의 끝
# r() : 정규표현식 regular expression
# r'^$' == ''
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls'))
]
