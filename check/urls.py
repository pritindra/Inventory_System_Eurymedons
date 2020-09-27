from django.urls import path
from check import views
from check.views import (
    HistoryView
)

urlpatterns = [
    path('checkin', views.checkin, name='checkin'),
    path('history', HistoryView.as_view(), name='history')
]