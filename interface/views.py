from django.shortcuts import render
import sys

# Create your views here.
def cover(request):
    return render(request, "interface/cover.html")

def dashboard(request):
    return render(request, "interface/dashboard.html")

def categories(request):
    return render(request, "interface/categories.html")

def check(request):
    return render(request, "interface/check.html")


def arsenal(request):
    return render(request, "interface/arsenal.html")