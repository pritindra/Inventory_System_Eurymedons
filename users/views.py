from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import sys
from users.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filter import UserFilter

# C


# # Create your views here.
# def signin(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username,password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('interface/dashboard')

#         else:
#             return redirect('users/signin')

#     else:
#         return render(request,'users/signin.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')

# class profile(DetailView,LoginRequiredMixin):
#     model = UserInfo
#     template_name = 'users/profile.html'
#     context_object_name = 'user'

def signout(request):
    auth.logout(request)
    return redirect('')

# class UserList(ListView):
#     model = UserInfo
#     template_name = 'users/user-list.html'
#     context_object_name = 'users'
    
def user_list(request):
    user_list = UserInfo.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'users/user_filter.html', {'filter': user_filter})