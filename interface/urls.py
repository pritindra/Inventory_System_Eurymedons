from django.urls import path
from interface import views

urlpatterns = [
    path('', views.cover, name='cover'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('categories', views.categories, name='categories'),
    path('check', views.check, name='check'),
    path('arsenal', views.arsenal, name='arsenal')

]
