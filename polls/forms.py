# -*- coding:utf-8 -*-
# --author:'xiawei'
# --date: '2017/9/15'

from django import forms

from polls.models import Question


class StudentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    sex = forms.CharField(label='sex', max_length=20)
    age = forms.IntegerField(label='age', max_value=100)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
