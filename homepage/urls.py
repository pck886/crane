# -*- coding: utf-8 -*-
from django.conf.urls import url


from homepage import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^post/(?P<pk>\d+)/$', views.home, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
