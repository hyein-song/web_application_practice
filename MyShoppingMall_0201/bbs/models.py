from django.db import models

# Create your models here.
# bbs_post 라는 이름의 table로 db에 생성됨


class Post(models.Model):
    author = models.CharField('작성자', max_length=20)
    contents = models.CharField('글 내용', max_length=100)

    def __str__(self):
        return self.contents
