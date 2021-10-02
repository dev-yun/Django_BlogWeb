from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from namecard.models import Namecard_TBL


class NamecardLV(ListView):
    model = Namecard_TBL


class NamecardDV(DetailView):
    model = Namecard_TBL
