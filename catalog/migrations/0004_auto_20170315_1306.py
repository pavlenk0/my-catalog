# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170314_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='''13 Character\n
                                   <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>''',
                                   max_length=13, verbose_name='ISBN'),
        ),
    ]
