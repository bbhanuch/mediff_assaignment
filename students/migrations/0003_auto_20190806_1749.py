# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-06 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190806_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
    ]
