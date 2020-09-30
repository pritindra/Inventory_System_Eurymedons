from django.shortcuts import render, get_object_or_404
from interface.models import Arsenal, Vehicles, Criminal
import sys
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def cover(request):
    return render(request, "interface/cover.html")

@login_required
def contact(request):
    return render(request, "interface/contact.html")

@login_required
def categories(request):
    return render(request, "interface/categories.html")

@login_required
def check(request):
    return render(request, "interface/check.html")

class ArsenalView(ListView,LoginRequiredMixin):
    model = Arsenal
    template_name = 'interface/arsenal.html'
    context_object_name = 'arsenals'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data


class VehiclesView(ListView,LoginRequiredMixin):
    model = Vehicles
    template_name = 'interface/vehicles.html'
    context_object_name = 'vehicles'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class CriminalView(ListView,LoginRequiredMixin):
    model = Criminal
    template_name = 'interface/criminal.html'
    context_object_name = 'criminals'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class ArsenalMoreInfo(DetailView,LoginRequiredMixin):
    model = Arsenal
    template_name = 'interface/more_info.html'
    context_object_name = 'arsenal'
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

class VehicleMoreInfo(DetailView,LoginRequiredMixin):
    model = Vehicles
    template_name = 'interface/more_info_vehicles.html'
    context_object_name = 'vehicle'

class CriminalMoreInfo(DetailView,LoginRequiredMixin):
    model = Criminal
    template_name = 'interface/more_info_criminals.html'
    context_object_name = 'criminal'
    
@login_required
def help(request):
    return render(request, "interface/help.html")

