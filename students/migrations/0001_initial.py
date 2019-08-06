# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-06 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_roll_number', models.IntegerField()),
                ('student_name', models.CharField(max_length=50)),
                ('student_age', models.IntegerField()),
                ('student_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
            ],
        ),
    ]