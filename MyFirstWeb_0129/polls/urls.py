
from django.urls import path
from . import views

app_name = 'polls'   # 일반적으로 application 이름으로 설정함 (url을 계층구조로 관리하기 위해서)

urlpatterns = [
    path('', views.index, name='index'),   # polls/     polls:index(namespace)
    path('<int:question_id>/', views.detail, name='detail'),      # polls/1/      변하는값이 온다
    path('<int:question_id>/vote/', views.vote, name='vote'),       # polls:vote
    path('<int:question_id>/results/', views.results, name='results')       # polls:vote
]

