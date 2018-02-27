from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    )
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponse,
    JsonResponse
    )
from .forms import (
    AuthForm,
    SignupForm,
    SignupProfileForm,
    GroupProfileForm
    )

from django.urls import reverse
from django.conf import settings
from .models import Profile
from search.models import (
    Play,
    Review,
    Theater
    )

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

## 여기서 내가 좋아요 한  파일을 가져올 수 있어야 함
## 유저를 가져와야 하는구나

def profile_detail(request, username):
    profile = Profile.objects.all()
    my_profile = profile.get(user__username=username)
    follower = my_profile.follow.all()

    review = []
    review_play = []
    for i in follower:
        for j in list(Review.objects.filter(author_id=i.user.pk)):
            if j.play.playid not in review_play:
                review.append(j)
                review_play.append(j.play.playid)

    play = Play.objects.all()
    play_to_my_heart = play.filter(to_my_heart__username=username)

    review_user = Review.objects.filter(author_id=my_profile.user.pk)


    tag_user = set()
    for a in review_user:
        tag_user |= set(a.tag.all())

    # review_follower = review.filter(author_id=follower.user_id)
    print(play_to_my_heart.all())
    print(review)
    ctx = {
        'review_profile':review_user,
        'review_user':tag_user,
        'play_to_my_heart':play_to_my_heart.all(),
        'profile':my_profile,
        'follower_review':review,
        'play':play,
        }
    # play_to_select = play_to_my_heart.get('name')

    return render(request, 'accounts/profile.html', ctx)


def login_and_redirect_next(request, user):
    auth_login(request, user)
    next_url = request.GET.get('next') or settings.LOGIN_REDIRECT_URL
    return redirect(next_url)


def signup(request):
    signup_form = SignupForm(request.POST or None)
    profile_form = SignupProfileForm(request.POST or None, request.FILES or None)

    if request.method == 'GET':
        if request.is_ajax():
            if request.GET['theater'] == 'true':
                profile_form = GroupProfileForm()
            return render(request, 'accounts/form.html', {
                'signup_form': signup_form,
                'profile_form': profile_form,
                })
    else:
        if request.is_ajax():
            pk = int(request.POST.get('theater'))
            theater = Theater.objects.get(pk=pk)
            return JsonResponse({'lat': theater.latitude,
                'lng': theater.longitude})
        elif signup_form.is_valid():
            if request.POST.get('is_groupuser'):
                print(request.POST.get('is_groupuser'))
                profile_form = GroupProfileForm(request.POST, request.FILES or None)
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

## 개인 유저는 왜?? 가입시에 사진  첨부가 안되는지??
## 개인 유저는 프로필 수정시에 왜??

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
        'form': form,
        'profile': Profile.objects.get(user=request.user)
    }
    return render(request, 'accounts/profile_create.html', ctx)


@login_required
def follow(request, pk):
    if request.method == "POST":
        follow = Profile.objects.get(user__pk=pk)
        print(follow)
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


@login_required
def cardnews(request):
    if request.method == "POST":
        print(request.POST)
        profile = Profile.objects.filter(user=request.user)
        genre = request.POST.getlist('genre[]')
        character = request.POST.getlist('character[]')
        profile.update(genre_select=genre, play_char=character)
        print(genre)
        print(character)

    return render(request, 'accounts/cardnews.html')

@login_required
def cardnews_2(request):
    if request.method == "POST":
        actor = request.POST.get('actor')
        staff = request.POST.get('staff')
        price = int(request.POST.get('price'))
        profile = Profile.objects.filter(user=request.user)
        profile.update(liebe_t=staff, liebe_a=actor, price=price)
        return redirect(reverse('search:recommend'))
    return render(request, 'accounts/cardnews2.html')
