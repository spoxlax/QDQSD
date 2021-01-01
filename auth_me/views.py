from django.shortcuts import render, redirect
from .fomrs import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# this fuction to test ( URLS, Rendring, REdirection, .... etc )
def test(request):
    return render(request, 'auth_me/signup_success.html')


# end Comment


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "GET":
        return render(request, 'auth_me/login.html', context)
    if request.method == "POST":
        if form.is_valid():
            log = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user_log = authenticate(request,username=log,password=password)
            if user_log is not None:
                login(request,user_log)
                return redirect ('/test')
            else:
                print("error login")
    return render(request, 'auth_me/signup.html', context)


def signup_page(request):
    form = SignupForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "GET":
        return render(request, 'auth_me/signup.html', context)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username, email, password)
            return render(request, 'auth_me/signup_success.html', context)
    return render(request, 'auth_me/signup.html', context)
