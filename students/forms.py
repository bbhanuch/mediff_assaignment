from django import forms
from models import Student

class StudentForm(forms.ModelForm):
    # student_roll_number = forms.IntegerField(min_value=0,max_value=50)
    # student_name = forms.CharField(max_length=50)
    # student_age = forms.IntegerField()
    # gender_choices = (("Male","Male"),
    #                   ("Female", "Female"))
    # student_gender = forms.ChoiceField(choices=gender_choices)
    class Meta:
        model = Student
        fields = ["student_roll_number", "student_name", "student_age", "student_gender"]
