from django.db import models

# Create your models here.
class Question(models.Model) :
    # 이렇게 정의되는 class가 데이터베이스의 table과 mapping됨
    # table의 column은 속성으로 표현
    question_text = models.CharField(max_length=200)        # 문자열 들어가는 field(200자를 넘을 수 없다)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text


class Choice(models.Model) :
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # foreign key 는 _id 가 나중에 자동으로 붙음
    question = models.ForeignKey(Question, on_delete=models.CASCADE)



    def __str__(self):
        return self.choice_text



