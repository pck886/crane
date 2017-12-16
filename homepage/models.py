# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.xlsx', '.xls', '.pdf', '.hwp']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'업로드 불가능한 파일형식 입니다.')


def user_path(instance, filename):  # 파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)  # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1]  # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    if extension in ['.xlsx', '.xls']:
        return 'xls/%s/%s.%s' % (timezone.now().strftime('%Y%m%d'), pid, extension)  # 예 : wayhome/abcdefgs.png

    return 'img/%s/%s.%s' % (timezone.now().strftime('%Y%m%d'), pid, extension)  # 예 : wayhome/abcdefgs.png


class Home(models.Model):
    author = models.ForeignKey(User, default=User, verbose_name='작성자')
    photo = models.ImageField(upload_to=user_path, verbose_name='메인사진')
    title = models.CharField(max_length=200, verbose_name='메인제목')
    text = models.TextField(verbose_name='메인내용')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ('created_date',)
        get_latest_by = ('created_date',)
        verbose_name_plural = '메인페이지'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


class About(models.Model):
    author = models.ForeignKey(User, default=User, verbose_name='작성자')
    photo = models.ImageField(upload_to=user_path, blank=True)
    title = models.CharField(max_length=200, default='', blank=True, verbose_name='회사소개 제목')
    text = models.TextField(verbose_name='회사소개 내용', blank=True)
    history_title = models.CharField(max_length=200, default='', blank=True, verbose_name='연혁 제목')
    history_sub_title = models.CharField(max_length=200, default='', blank=True, verbose_name='연혁 부제목')
    history_text = models.TextField(verbose_name='연혁 내용')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ('created_date',)
        get_latest_by = ('created_date',)
        verbose_name_plural = '회사소개'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


class EquipmentIntro(models.Model):
    author = models.ForeignKey(User, default=User, verbose_name='작성자')
    model = models.CharField(max_length=200, default='', verbose_name='장비이름')
    company = models.CharField(max_length=20, default='', verbose_name='제조회사')
    boom = models.FloatField(default=0, verbose_name='기본붐')
    singular = models.IntegerField(default=0, verbose_name='기본붐 단수')
    radius = models.FloatField(default=0, verbose_name='최대작업반경')
    capacity = models.FloatField(default=0, verbose_name='최대인양능력')
    xls_file = models.FileField(upload_to=user_path, blank=True, validators=[validate_file_extension], verbose_name='엑셀파일')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ('created_date',)
        get_latest_by = ('created_date',)
        verbose_name_plural = '장비소개'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.model


class CompanyInfo(models.Model):
    author = models.ForeignKey(User, default=User, verbose_name='작성자')
    name = models.CharField(max_length=200, default='', verbose_name='회사이름')
    address = models.CharField(max_length=20, default='', verbose_name='회사주소')
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True, verbose_name='이메일')
    delegate_number = models.CharField(max_length=20, default='', blank=True, verbose_name='대표전화번호')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ('created_date',)
        get_latest_by = ('created_date',)
        verbose_name_plural = '회사정보'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.name


class Cta(models.Model):
    name = models.CharField(max_length=20, default='', verbose_name='이름')
    phone = models.CharField(max_length=20, default='', blank=True, verbose_name='전화번호')
    email = models.EmailField(max_length=70, blank=True, null=True, verbose_name='이메일')
    subject = models.CharField(max_length=200, default='', verbose_name='제목')
    message = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    modified_date = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ('created_date',)
        get_latest_by = ('created_date',)
        verbose_name_plural = '문의사항'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.subject


class Images(models.Model):
    image_list = models.ForeignKey(EquipmentIntro)
    image = models.ImageField(upload_to=user_path,  blank=True, validators=[validate_file_extension], verbose_name='장비사진')


class Equipments(models.Model):
    equipment_list = models.ForeignKey(About)
    name = models.CharField(max_length=200, default='', verbose_name='장비명')
    standard = models.CharField(max_length=200, default='', verbose_name='규격')
    form = models.CharField(max_length=200, default='', verbose_name='형식')
    producer = models.CharField(max_length=200, default='', verbose_name='제작사')

    class Meta:
        verbose_name_plural = '장비리스트'


class Phones(models.Model):
    phone_list = models.ForeignKey(CompanyInfo)
    number = models.CharField(max_length=100, default='', blank=True, verbose_name='전화번호')