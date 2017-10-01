# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Max
from django.shortcuts import render, get_object_or_404

from .models import Home, About
from .forms import PostForm


def home(request):
    homes = Home.objects.filter().order_by('pk')
    return render(request, 'homepage/index.html', {'homes': homes})


def about(request):
    abouts = About.objects.aggregate(pk=Max('pk'), title=Max('title'), text=Max('text'))
    return render(request, 'homepage/about.html', {'abouts': abouts})


def blog(request):
    return render(request, 'homepage/blog.html', {})


def post_new(request):
    form = PostForm()
    return render(request, 'homepage/post_edit.html', {'form': form})
