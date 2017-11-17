# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 18:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beers', '0002_auto_20171116_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='beer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_beer_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='beer',
            name='last_modified_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='beer',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_beer_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_company_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='company',
            name='last_modified_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='company',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_company_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AddField(
            model_name='specialingredient',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='specialingredient',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_specialingredient_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='specialingredient',
            name='last_modified_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Last modified at'),
        ),
        migrations.AddField(
            model_name='specialingredient',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beers_specialingredient_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
    ]
