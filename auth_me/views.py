from django.shortcuts import render
from .fomrs import SignupForm


def login_page(request):
    return render(request, 'auth_me/login.html')


def signup_page(request):
    signup_form = SignupForm()
    context = {
        "form": signup_form
    }
    return render(request, 'auth_me/signup.html', context)
