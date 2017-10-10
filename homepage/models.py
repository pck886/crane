# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


def user_path(instance, filename):  # 파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)  # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1]  # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return 'img/%s/%s/%s.%s' % (instance.author, timezone.now().strftime('%Y%m%d'), pid, extension)  # 예 : wayhome/abcdefgs.png


class Home(models.Model):
    author = models.ForeignKey('auth.User', default='crane', verbose_name='작성자')
    photo = models.ImageField(upload_to=user_path, verbose_name='메인사진')
    title = models.CharField(max_length=200, verbose_name='메인제목')
    text = models.TextField(verbose_name='메인내용')
    created_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        verbose_name_plural = '메인페이지'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


class About(models.Model):
    author = models.ForeignKey('auth.User', default='crane')
    photo = models.ImageField(upload_to=user_path, blank=True)
    title = models.CharField(max_length=200, verbose_name='회사소개 제목')
    text = models.TextField(verbose_name='회사소개 내용')
    created_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        verbose_name_plural = '회사소개'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title


class EquipmentIntro(models.Model):
    author = models.ForeignKey('auth.User', default='crane')
    photo = models.ImageField(upload_to=user_path, blank=True, verbose_name='장비사진')
    model = models.CharField(max_length=200, default='', verbose_name='장비이름')
    company = models.CharField(max_length=20, default='', verbose_name='제조회사')
    boom = models.IntegerField(default=0, verbose_name='기본붐')
    radius = models.IntegerField(default=0, verbose_name='최대작업반경')
    capacity = models.IntegerField(default=0, verbose_name='최대인양능력')
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='등록일')

    class Meta:
        verbose_name_plural = '장비소개'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.model