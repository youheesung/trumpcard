from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    )
from .forms import SignupForm, AuthForm
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    )
from .models import Profile
from django.urls import reverse
from django.conf import settings
# Create your views here.


def login(request):
    form = AuthForm(request, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        next = request.GET.get('next') or request.path
        return login_and_redirect_next(request,user) ## 여기에 함수를 넣어서 다시하기
    ctx = {
        'form':form,
    }
    return render(request, 'login.html', ctx)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect(reverse('accounts:logout'))

# signup 하는 사이트
def signup(request):
    signup_form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if signup_form.is_valid():
            user = signup_form.save()
        return
    ctx = {
        'signup_form' : signup_form,
    }
    return render(request, 'signup.html', ctx)
# def login_and_redirect_next(request, user):

def login_and_redirect_next(request, user):
    auth_login(request, user)
    next_url =request.GET.get('next') or settings.LOGIN_REDIRECT_URL
    return redirect(next_url)

def profile_detail(request, username):
    ctx = {
        'profile': get_object_or_404(Profile,
            user__username=username)
    }
    return render(request, 'accounts/profile_detail.html',ctx)