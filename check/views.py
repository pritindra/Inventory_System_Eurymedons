from django.shortcuts import render
from django.contrib.auth.models import User
from check.models import ItemHistory
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def checkin(request):
    return render(request, "check/checkin.html")

class HistoryView(ListView):
    model = ItemHistory
    template_name = 'check/history.html'
    context_object_name = 'history'