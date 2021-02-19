from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.CharField('작성자', max_length=20)
    p_title = models.CharField('글 제목', max_length=100)
    p_contents = models.CharField('글 내용', max_length=300)
    p_date = models.DateTimeField('글 작성일')

    def __str__(self):
        return self.p_title
