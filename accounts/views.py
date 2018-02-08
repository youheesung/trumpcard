from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    )
from .forms import AuthForm
from django.urls import reverse
from django.conf import settings

# Create your views here.


def login(request):
    form = AuthForm(request, request.POST or None)
    if request.method == "POST" and form.is_valid():

        auth_login(request, form.get_user())
        next = request.GET.get('next') or settings.LOGIN_REDIRECT_URL

        return redirect(next)

    ctx = {
        'form': form
    }
    return render(request, 'accounts/login.html', ctx)


def logout(request):
    auth_logout(request)
    return redirect(reverse('accounts:login'))