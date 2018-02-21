from django.shortcuts import (
    render,
    redirect)
from django.urls import reverse
from .models import (
    Play,
    Review,
    Theater
    )
from .forms import (
    PlayForm,
    ReviewForm
    )

from django.http import HttpResponse
# Create your views here.


def search(request):
    form = PlayForm()
    box = Play.objects.order_by('grade')
    ctx = {
        'form': form,
        'box': box,
    }
    return render(request, 'search.html', ctx)


def result(request):
    if request.method == "POST":
        result = Play.objects.all()
        if request.POST.get('name'):
            result = result.filter(name__contains=request.POST.get('name'))
        if request.POST.get('actor'):
            result = result.filter(actor__contains=request.POST.get('actor'))
        if request.POST.get('staff'):
            result = result.filter(staff__contains=request.POST.get('staff'))
        if request.POST.get('place'):
            result = result.filter(place__contains=request.POST.get('place'))
        if request.POST.get('date'):
            result = result.filter(start_date__lte=request.POST.get('date'), end_date__gte=request.POST.get('date'))

        if request.POST.get('minprice'):
            result = result.filter(minprice__lte=request.POST.get('minprice'))

        ctx = {
            'result': result
        }
    return render(request, 'result.html', ctx)


def detail(request, playid):
    play = Play.objects.get(playid=playid)
    theater = Theater.objects.get(placeid=play.placeid)
    ctx = {
        'play': play,
        'theater': theater
    }
    return render(request, 'detail.html', ctx)


def review(request, pk=None, playid=None):
    if pk is None and playid is not None:
        review = Review.objects.filter(play__playid=playid)
    elif pk is not None and playid is None:
        review = Review.objects.filter(author__pk=pk)

    ctx = {
        'review': review,
        }
    return render(request, 'review.html', ctx)

## review_ form에 태그를 넣는 부분을 추가해야 하는가??
##

def review_create(request, playid):

    form = ReviewForm()
    play = Play.objects.filter(playid=playid)
    if request.method == 'POST' and request.is_ajax():
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.author = request.user
            new_review.play = play.get(playid=playid)
            new_review.save()
        review = Review.objects.filter(play__playid=playid)
        review_count = review.count()
        rateSum = 0
        for i in review:
            rateSum += i.rate
        rateSum /= review_count
        play.update(rate=rateSum)
    ctx = {
        'form': form,
        'play': play.get(playid=playid)
    }
    return render(request, 'review_create.html', ctx)

##


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    ctx = {
        'review': review,
    }
    return render(request, 'review_detail.html', ctx)



def play_create(request):
    form = PlayForm(request.POST or None)
    ctx = {
        'form': form,
    }
    return render(request, 'play_create.html', ctx)

def to_my_heart(request, playid):
    if request.method == "POST":
        play = Play.objects.get(playid=playid)
        if request.user.play_to_my_heart.filter(playid=playid).exists():
            play.to_my_heart.remove(request.user)
        else:
            play.to_my_heart.add(request.user)
        ctx = {
            'did_to_my_heart': request.user.play_to_my_heart.filter(playid=playid).exists(),
            'play': play
            }
        return render(request, 'to_my_heart_button.html', ctx)
    else:
        return HttpResponse(status=400)


