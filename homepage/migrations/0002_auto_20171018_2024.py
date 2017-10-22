# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 11:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=homepage.models.user_path, verbose_name='\uc7a5\ube44\uc0ac\uc9c4')),
                ('image_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='homepage.EquipmentIntro')),
            ],
        ),
        migrations.RemoveField(
            model_name='propertyimage',
            name='property',
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
    ]
