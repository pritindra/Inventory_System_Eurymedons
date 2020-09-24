from django.shortcuts import render

# Create your views here.
def checkin(request):
    return render(request, "check/checkin.html")