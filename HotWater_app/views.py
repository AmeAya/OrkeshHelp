from django.shortcuts import render
from .models import HotSprings
from django.views.generic import ListView

# Create your views here.
class HotWaterListView(ListView):
    model = HotSprings
    template_name = 'home.html'
