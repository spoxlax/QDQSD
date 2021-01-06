from django.shortcuts import render, redirect
from .fomrs import SignupForm, LoginForm
from django.contrib.auth import authenticate, login
from account.models import Account
from .name_resolver import resolver as solve


# this fuction to test ( URLS, Rendring, REdirection, .... etc )
def test(request):
    return render(request, 'dashboard.html')


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
            user_log = authenticate(request, username=log, email=log, password=password)
            if user_log is not None:
                login(request, user_log)
                return redirect('/test')
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
            name_resolver = solve(email)
            Account.objects.create_user(username=username, first_name=name_resolver.first_name,
                                        last_name=name_resolver.last_name, email=email, password=password)
            return render(request, 'auth_me/signup_success.html', context)
    return render(request, 'auth_me/signup.html', context)
