from django.urls import path
from users import views
from users.views import (
    
    profile
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', profile.as_view(), name='profile'),
    path('user-list', views.user_list, name='user-list'),
    path('pdf-view', views.html_to_pdf_view, name='pdf-view')
]