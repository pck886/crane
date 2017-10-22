# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Home, About, EquipmentIntro
from .forms import PostForm


def home(request):
    homes = Home.objects.filter().order_by('pk')
    return render(request, 'homepage/index.html', {'homes': homes})


def about(request):
    abouts = About.objects.aggregate(pk=Max('pk'), title=Max('title'), text=Max('text'))
    return render(request, 'homepage/about.html', {'abouts': abouts})


def equipment_intro(request):
    equipment_intros = EquipmentIntro.objects.all()

    if equipment_intros is None:
        return render(request, 'homepage/equipmentIntro.html', {'equipment_intros': equipment_intros})


    paginator = Paginator(equipment_intros, 5)  # Show 25 contacts per page

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'homepage/equipmentIntro.html', {'equipment_intros': contacts})


def equipment_intro_single(request):
    form = PostForm()
    return render(request, 'homepage/equipmentIntro-single.html', {'form': form})
