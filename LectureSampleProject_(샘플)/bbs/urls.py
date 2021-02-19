from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    path('list/', views.p_list, name='p_list'),
    path('create/', views.p_create, name='p_create'),
    path('detail/<int:post_id>', views.p_detail, name='p_detail'),
    path('delete/<int:post_id>', views.p_delete, name='p_delete'),
    path('update/<int:post_id>', views.p_update, name='p_update'),
]
