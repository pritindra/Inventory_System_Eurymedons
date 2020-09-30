from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import sys
from users.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filter import UserFilter
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML
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


# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')

class profile(ListView,LoginRequiredMixin):
    model = UserInfo
    template_name = 'users/profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        return data

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


def html_to_pdf_view(request):
    user_list = UserInfo.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    html_string = render_to_string('users/user_filter.html', {'filter': user_filter})

    html = HTML(string=html_string).write_pdf()
    # html.write_pdf(target='home/drex/Desktop/designs/mypdf.pdf')

    # fs = FileSystemStorage('/home/drex/Desktop/designs')
    # with fs.open('mypdf.pdf') as pdf:
    response = HttpResponse(html, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    return response

    # return response