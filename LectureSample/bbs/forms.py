# 여기서는 ModelForm class를 정의해요!
# ModelForm이 자동으로 Form field(HTML tag)를 생성해줘요
# Form 처리를 상당히 간단하게 처리할 수 있어요!
# from importlib import import_module
# from django.conf import settings

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'author_name', 'p_title', 'p_contents', 'p_date']
        widgets = {
            'author': forms.HiddenInput(),
            'author_name': forms.HiddenInput(),
            'p_title': forms.TextInput(attrs={'id': 'p_title',
                                              'class': 'form-control'}),
            'p_contents': forms.TextInput(attrs={'id': 'p_contents',
                                                 'class': 'form-control'}),
            'p_date': forms.HiddenInput()
        }

        labels = {
            'p_title': '글 제목',
            'p_contents': '글 내용'
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author_name'].widget.attrs['maxlength'] = 10
        self.fields['author_name'].required = False
        self.fields['p_date'].required = False
        self.fields['author'].required = False
