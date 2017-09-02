from django import forms
from .models import Comment

class CommentForm(forms.ModelForm): #表单继承自表单类
    class Meta:
        model =Comment    #对应的数据库模型是Comment
        fields=['name','email','url','text']  #指定了表单需要显示的字段