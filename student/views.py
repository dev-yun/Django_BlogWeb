from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from student.models import Student


class StudentLV(ListView):
    model = Student


class StudentDV(DetailView):
    model = Student
