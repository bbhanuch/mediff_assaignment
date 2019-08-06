# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import StudentForm
from models import Student
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from constants import *


# Create your views here.
def insert_view(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # student_rno = form.cleaned_data["student_roll_number"]
            # print student_rno
            # student_name = form.cleaned_data["student_name"]
            # print student_name
            # student_gender = form.cleaned_data["student_gender"]
            # student_age = form.cleaned_data["student_age"]
            # Inserting data into dictionary
            # save_details(student_rno, student_name, student_age, student_gender)
            return HttpResponse("<h2>Yay..! data inserted successfully</h2>")
    else:
        form = StudentForm()
    return render(request, "insert.html", {"form": form})


def display(request):
    recs = Student.objects.all()
    return render(request, 'display.html', {'records':recs})


def delete(request):
    roll_num = int(request.GET['roll_num'])
    record = get_object_or_404(Student, pk=roll_num)
    record.delete()
    return HttpResponse("<h2>Record Deleted .. !</h2>")
    # try:
    #     query = Student.objects.get(student_roll_number=roll_num)
    #     query.delete()
    #     return HttpResponse("Record Deleted")
    # except Student.DoesNotExist:
    # return HttpResponse("Student with the given roll number does not exists")


def search(request):
    roll_num = int(request.GET['roll_num'])
    record = get_object_or_404(Student, pk=roll_num)
    # return HttpResponse("<ul><li>Name - %s</li><li>Age - %d</li><li>Gender - %s</li></ul>"%
    #                     (record.student_name, record.student_age, record.student_gender))
    return render(request, "search.html", {"rec": record})