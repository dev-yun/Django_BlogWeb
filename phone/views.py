from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from phone.models import Phone


class PhoneLV(ListView):
    model = Phone


class PhoneDV(DetailView):
    model = Phone
