from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.CharField('작성자', max_length=20)
    contents = models.CharField('글 내용', max_length=200)

    def __str__(self):
        return self.contents


