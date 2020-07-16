from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from core.forms import RegistrationForm


def test(request):
    return HttpResponse("test-page")


def home(request):
    return redirect("products")


def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    context = {}
    if "login" in request.POST:
        form = AuthentionForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(user)
            return redirect(home)

    context["form"] = AuthenticationForm()
    return render(request, "core/login.html", context)


def logout(request):
    auth.logout(request)
    return redirect(home)