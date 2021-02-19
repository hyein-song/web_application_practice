from django.db import models
from django.contrib.auth.models import User

# 기존 User 모델과 OneToOneField로 일대일관계를 맺는 모델을 추가해서
# 사용자에 관한 추가 정보(전화번호, 성별)를 저장
# 가장 쉬운 방법(이것외에 프록시 모델 기법, AbstractUser, AbstractBaseUser를 상속하는
# 방법이 있다.)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
