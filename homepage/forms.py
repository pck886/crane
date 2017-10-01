# -*- coding: utf-8 -*-

from django import forms
from .models import Home

class PostForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = ('title', 'text')