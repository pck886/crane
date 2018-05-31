# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Home, About, EquipmentIntro, Images, Equipments, Phones, CompanyInfo, Cta, BoardImage, BoardImages


class BoardImagesInline(admin.TabularInline):
    model = BoardImages
    fields = ['board_image', ]
    extra = 4
        

class ImagesInline(admin.TabularInline):
    model = Images
    fields = ['image', ]
    extra = 4


class EquipmentListInline(admin.TabularInline):
    model = Equipments
    fields = ['name', 'standard', 'form', 'producer', ]
    extra = 4


class PhonesInline(admin.TabularInline):
    model = Phones
    fields = ['number', ]
    extra = 4


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class AboutAdmin(admin.ModelAdmin):
    inlines = [EquipmentListInline, ]
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    search_fields = ('title',)



class EquipmentIntroAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, ]
    list_display = ('id', 'model', 'company', 'boom', 'radius', 'capacity', 'xls_file', 'created_date')
    list_display_links = ('id', 'model')
    search_fields = ('model',)


class CompanyInfoAdmin(admin.ModelAdmin):
    inlines = [PhonesInline, ]
    list_display = ('id', 'name', 'address', 'created_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CtaAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'message', 'name', 'email', 'created_date')
    list_display_links = ('id', 'subject')
    search_fields = ('subject', 'message',)


class BoardImageAdmin(SummernoteModelAdmin):
    inlines = [BoardImagesInline, ]
    list_display = ('id', 'subject', 'created_date', 'modified_date')
    list_display_links = ('id', 'subject')
    search_fields = ('subject', 'image_text',)
    ordering = ('-created_date',)
    summernote_fields = ('image_text', )

# Apply summernote to all TextField in model.
# class SomeModelAdmin(SomeModelAdmin):
#    summernote_fields = '__all__'


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(EquipmentIntro, EquipmentIntroAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Cta, CtaAdmin)
admin.site.register(BoardImage, BoardImageAdmin)
#admin.site.register(SomeModel, SomeModelAdmin)
