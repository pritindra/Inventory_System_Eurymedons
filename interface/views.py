from django.shortcuts import render, get_object_or_404
from interface.models import Arsenal, Vehicles
import sys
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def cover(request):
    return render(request, "interface/cover.html")

def contact(request):
    return render(request, "interface/contact.html")

def dashboard(request):
    return render(request, "interface/dashboard.html")

def categories(request):
    return render(request, "interface/categories.html")

def check(request):
    return render(request, "interface/check.html")

class ArsenalView(ListView):
    model = Arsenal
    template_name = 'interface/arsenal.html'
    context_object_name = 'arsenals'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data


class VehiclesView(ListView):
    model = Vehicles
    template_name = 'interface/vehicles.html'
    context_object_name = 'vehicles'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class ArsenalMoreInfo(DetailView):
    model = Arsenal
    template_name = 'interface/more_info.html'
    context_object_name = 'arsenal'

class VehicleMoreInfo(DetailView):
    model = Arsenal
    template_name = 'interface/more_info_vehicles.html'
    context_object_name = 'vehicle'
    

def help(request):
    return render(request, "interface/help.html")

