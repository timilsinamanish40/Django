from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# def home(request):
#     return HttpResponse("Hello Everyone")
def home(request):
    return render(request, 'home/welcome.html' , {'today' : datetime.today()})
def about(request):
    return render(request, 'home/about.html')

@login_required(login_url='/admin') # if not logged in, it will redirect to admin login page
def authorized(request):
    return render(request, 'home/authorized.html', {})
