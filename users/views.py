from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
import sys

# Create your views here.
def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('interface/dashboard')

        else:
            return redirect('users/signin')

    else:
        return render(request,'users/signin.html')


def signout(request):
    auth.logout(request)
    return redirect('')