# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from django.http import JsonResponse
from django.db.models import Q
from .serializers import SnippetSerializer

from .models import Home, About, EquipmentIntro, CompanyInfo, BoardImage
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
    imageboards = BoardImage.objects.all()
    company = CompanyInfo.objects.order_by('pk').first()

    if imageboards is None:
        return render(request, 'homepage/imageBoard.html', {'imageboards': imageboards, 'company': company})

    paginator = Paginator(imageboards, 5)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'homepage/imageBoard.html', {'imageboards': contacts, 'company': company})


def image_board_single(request):
    id = '%d' % request.GET.get('id', '')
    imageboard = BoardImage.objects.get(pk=id)
    company = CompanyInfo.objects.order_by('pk').first()

    return render(request, 'homepage/imageBoardSingle.html', {'imageboard': imageboard, 'company': company})


def search_image_board(request):
    search_word = request.GET.get('search_word', '')
    company = CompanyInfo.objects.order_by('pk').first()

    if search_word:

        image_content = BoardImage.objects.filter(Q(subject__contains=search_word) |
                                                  Q(image_text__contains=search_word)).distinct().order_by('modified_date')


    paginator = Paginator(image_content, 5)

    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'homepage/imageBoard.html', {'imageboards': contacts, 'search_word': search_word, 'company': company})






def equipment_intro_single(request):
    form = PostForm()
    return render(request, 'homepage/equipmentIntro-single.html', {'form': form})
