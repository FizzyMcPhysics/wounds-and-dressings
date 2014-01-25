from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Wound, Dressing


# Create your views here.
class WoundListView(ListView):
    model = Wound


class DressingListView(ListView):
    model = Dressing


class DressingDetailView(DetailView):
    model = Dressing
    slug_field = "name"