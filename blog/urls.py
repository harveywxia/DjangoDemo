# -*- coding:utf-8 -*-
# --author:'xiawei'
# --date: '2017/9/28'

from django.conf.urls import url, include
from . import views
# this is the url namespace

url_personal_center = [
    url(r'^$', views.personal_center, name='personal_center'),
    url(r'^my_blog/$', views.my_blog, name='my_blog'),
    url(r'^create_blog/$', views.CreateBlogView.as_view(), name='create_blog'),
]

app_name = 'blog'
urlpatterns = [
    # ex:/blog/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_id>[0-9]+)/detail$', views.detail, name='detail'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),

    url(r'^save_blog/$', views.saveblog, name='save_blog'),
    url(r'^success/$', views.success, name='success'),
    url(r'^blog_search/$', views.blog_search, name='blog_search'),

    url(r'^personal_center/', include(url_personal_center)),
]
