# -*- coding:utf-8 -*-
# --author:'xiawei'
# --date: '2017/9/28'
from django import forms
from blog.models import Blog


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'username']
        # exclude = ['username']
