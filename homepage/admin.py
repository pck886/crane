# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Home, About, EquipmentIntro


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class EquipmentIntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'company', 'boom', 'radius', 'capacity', 'photo', 'created_date')
    list_display_links = ('id', 'model')
    search_fields = ('model',)


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(EquipmentIntro, EquipmentIntroAdmin)
