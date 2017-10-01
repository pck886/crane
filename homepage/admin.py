# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Home, About


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
