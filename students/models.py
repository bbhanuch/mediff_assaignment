# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    student_roll_number = models.IntegerField(primary_key=True,max_length=2)
    student_name = models.CharField(max_length=50)
    student_age = models.IntegerField(max_length=2)
    gender_choices = (("Male", "Male"),
                      ("Female", "Female"))
    student_gender = models.CharField(choices=gender_choices,max_length=6,default="Male")
