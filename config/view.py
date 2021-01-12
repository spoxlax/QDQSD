from django.shortcuts import render
from django.contrib import auth

def home_page(request):
    return render(request, 'Amer/dashboard.html')


def faq_page(request):
    return render(request, 'Amer/dashboard.html')


def logout(request):
    auth.logout(request)
    return render(request, 'Amer/dashboard.html')

def dashboard (request) :
    return render(request,'Amer/dashboard.html')