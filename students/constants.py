from collections import OrderedDict

StudentsDict = OrderedDict


def save_details(student_rno, student_name, student_age, student_gender):
    StudentsDict[student_rno] = {"student_name": student_name,
                                 "student_age": student_age,
                                 "student_gender": student_gender}