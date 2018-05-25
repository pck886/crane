# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from homepage import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^equipment_intro/$', views.equipment_intro, name='equipment_intro'),
    url(r'^equipment_intro_single/(?P<pk>\d+)/$', views.equipment_intro_single, name='equipment_intro_single'),
    url(r'^cta/$',views.cta, name='cta'),
    url(r'^image_board/$',views.image_board, name='image_board'),
    url(r'^search_image_board/$',views.search_image_board, name='search_image_board'),
    url(r'^image_board_single/$',views.image_board_single, name='image_board_single'),
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="project_robots_file"),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
]
