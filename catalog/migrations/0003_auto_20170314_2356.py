# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 21:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_auto_20170314_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='''13 Character\n
                                   <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>''',
                                   max_length=13, verbose_name='ISBN'),
        ),
    ]
