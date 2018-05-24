# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.http import JsonResponse
from .serializers import SnippetSerializer

from .models import Home, About, EquipmentIntro, CompanyInfo, ImageBoard
from .forms import PostForm


def home(request):
    homes = Home.objects.filter().order_by('pk')
    company = CompanyInfo.objects.order_by('pk').first()
    return render(request, 'homepage/index.html', {'homes': homes, 'company': company})


def about(request):
    abouts = About.objects.order_by('pk').first()
    company = CompanyInfo.objects.order_by('pk').first()
    return render(request, 'homepage/about.html', {'abouts': abouts, 'company': company})


def equipment_intro(request):
    equipment_intros = EquipmentIntro.objects.all()
    company = CompanyInfo.objects.order_by('pk').first()

    if equipment_intros is None:
        return render(request, 'homepage/equipmentIntro.html', {'equipment_intros': equipment_intros, 'company': company})


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

    return render(request, 'homepage/equipmentIntro.html', {'equipment_intros': contacts, 'company': company})


def cta(request):
    if request.method == 'POST':
        serializer = SnippetSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

    return JsonResponse(serializer.errors, status=400)


def image_board(request):
    images = ImageBoard.objects.all()
    company = CompanyInfo.objects.order_by('pk').first()

    if images is None:
        return render(request, 'homepage/imageBoard.html', {'images': images, 'company': company}})

    paginator = Paginator(images, 5)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'homepage/imageBoard.html', {'images': images, 'company': company}})


def image_board_sigle(request):
    return render(request, 'homepage/imageBoardSigle.html')


def equipment_intro_single(request):
    form = PostForm()
    return render(request, 'homepage/equipmentIntro-single.html', {'form': form})
