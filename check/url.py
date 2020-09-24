from django.urls import path
from check import views


urlpatterns = [
    path('checkin', views.checkin, name='checkin')
]
