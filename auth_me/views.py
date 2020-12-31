from django.shortcuts import render
from .fomrs import SignupForm


def login_page(request):
    return render(request, 'auth_me/login.html')


def signup_page(request):
    signup_form = SignupForm(request.POST)
    context = {
        "form": signup_form,
    }
    if request.method == "GET":
        return render(request, 'auth_me/signup.html', context)

    elif request.method == "POST":
        if signup_form.is_valid():
            return render(request, 'auth_me/signup.html', context)
    else:
        print(" unvalid data")
        return render(request, 'auth_me/signup.html', context)
