from django.shortcuts import render
from student.models import Student
from .serializers import StudentSerializer      
from rest_framework import viewsets


class StudentViewSet(viewsets.ModelViewSet):
	queryset=Student.objects.all()
	serializer_class=StudentSerializer
