from django.urls import path
from . import views

app_name = 'movieboxoffice'

urlpatterns = [
    path('search/', views.search, name='search')
]
