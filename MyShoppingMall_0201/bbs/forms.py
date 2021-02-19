# 여기서는 Modelform class를 정의함
# Model form이 자동으로 form field(html tag)를 생성해줌
# form 처리를 상당히 간단하게 처리할 수 있다.

from django import forms
from bbs.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'contents']



