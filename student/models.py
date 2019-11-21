from django.db import models
from course.models import Course
from django.core.exceptions import ValidationError
import datetime


class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    registration_number=models.CharField(max_length=50)
    place_of_residence=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    guardian_phone=models.CharField(max_length=50)
    id_number=models.IntegerField()
    date_joined=models.DateField()
    courses=models.ManyToManyField(Course, blank=True, related_name='students')
    image=models.ImageField(upload_to="student_image",blank=True)

    def full_name(self):
        # return self.first_name
        return "{} {}".format(
            self.first_name,                                                
            self.last_name)


    def __str__(self):
        return self.first_name

    def teachers(self):
        return[course.teacher for course in self.courses.all()]

