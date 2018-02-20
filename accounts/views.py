from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    )
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import (
    AuthForm,
    SignupForm,
    SignupProfileForm,
    GroupProfileForm
    )

from django.urls import reverse
from django.conf import settings
from .models import Profile

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


def profile_detail(request, username):
    ctx = {
        'profile': Profile.objects.get(user__username=username)
    }
    return render(request, 'accounts/profile.html', ctx)


def login_and_redirect_next(request, user):
    auth_login(request, user)
    next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
    return redirect(next_url)


def signup(request):
    signup_form = SignupForm(request.POST or None)
    profile_form = SignupProfileForm(request.POST or None)

    if request.method == 'POST':
        if request.is_ajax():
            if request.POST['theater'] == 'true':
                profile_form = GroupProfileForm()
            return render(request, 'accounts/form.html', {
                'signup_form': signup_form,
                'profile_form': profile_form,
                })
        if signup_form.is_valid():
            if request.POST.get('is_groupuser'):
                print(request.POST.get('is_groupuser'))
                profile_form = GroupProfileForm(request.POST)
            if profile_form.is_valid():
                user = signup_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return login_and_redirect_next(request, user)
    ctx = {
        'signup_form': signup_form,
        'profile_form': profile_form,
    }
    return render(request, 'accounts/signup.html', ctx)


@login_required
def profile_update(request, username):
    if request.user.profile.is_groupuser:
        form = GroupProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    else:
        form = SignupProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('accounts:profile_detail', kwargs={
            'username': username,
            }))

    ctx = {
        'form': form
    }
    return render(request, 'accounts/profile_create.html', ctx)


def follow(request, pk):
    if request.method == "POST":
        follow = Profile.objects.get(user__pk=pk)
        if request.user.profile.follow.filter(user__pk=pk).exists():
            request.user.profile.follow.remove(follow)
        else:
            request.user.profile.follow.add(follow)
        ctx = {
            'did_follow': request.user.profile.follow.filter(user__pk=pk).exists(),
        }
        return render(request, 'accounts/follow_button.html', ctx)
    else:
        return HttpResponse(status=404)

