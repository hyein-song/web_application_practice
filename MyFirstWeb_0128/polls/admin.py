from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
admin.site.register(Question)   #admin site에 class 등록
admin.site.register(Choice)   #admin site에 class 등록



