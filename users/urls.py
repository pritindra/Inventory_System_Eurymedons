from django.urls import path
from users import views

urlpatterns = [
    path('signin', views.signin, name='signin')
]