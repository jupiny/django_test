# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-23 11:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0001_initial'),
        ('posts', '0003_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_user_set',
            field=models.ManyToManyField(related_name='like_post_set', through='likes.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
