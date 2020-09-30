from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ItemChartView(TemplateView,LoginRequiredMixin):
    template_name='dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context["qs"]= Item.objects.all()
        return context
    