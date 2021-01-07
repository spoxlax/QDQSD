from django.shortcuts import render
from django.contrib import auth

def home_page(request):
    return render(request, 'home.html')


def faq_page(request):
    return render(request, 'faq.html')


def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def dashboard (request) :
    return render(request,'dashboard.html')