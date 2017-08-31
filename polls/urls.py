# -*- coding:utf-8 -*-
# --author:'xiawei'
# --date: '2017/8/30'
from django.conf.urls import url
from . import views

# this is the url namespace
app_name = 'polls'
urlpatterns = [
    # ex:/polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    # ?P<question_id> defines the name that will be used to identify the matched pattern'[0-9]+'
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
