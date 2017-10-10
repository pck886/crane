# -*- coding: utf-8 -*-
from django.conf.urls import url


from homepage import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^equipment_intro/$', views.equipment_intro, name='equipment_intro'),
    url(r'^equipment_intro_single/(?P<pk>\d+)/$', views.equipment_intro_single, name='equipment_intro_single'),
]
