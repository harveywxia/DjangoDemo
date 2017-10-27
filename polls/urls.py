# -*- coding:utf-8 -*-
# --author:'xiawei'
# --date: '2017/8/30'
from django.conf.urls import url, include
from . import views

url_extra = [
    # url like this: /polls/algorithm/?p1=algorithm1&p2=para1
    url(r'^$', views.algorithm, name='algorithm'),
    # url like this: /polls/algorithm/algorithm/alg_name=algorithm&para1=parameter
    url(r'^algorithm/alg_name=(?P<alg_name>.+)&para1=(?P<para1>.+)/$', views.algorithm2, name='algorithm2'),

    url(r'^test/', views.test, name='test'),
]

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

    url(r'^algorithm/', include(url_extra)),


    url(r'^login$', views.login, name='login'),
    url(r'^loginresult$', views.loginresult, name='loginresult'),

    url(r'^student$', views.get_student, name='student'),
    url(r'^nameinfo', views.nameinfo, name='nameinfo'),
]


