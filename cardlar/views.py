from django.shortcuts import render
from django.views.generic import ListView
from .models import Shaxs

class ShaxsListView(ListView):
  model = Shaxs
  template_name = 'home.html'