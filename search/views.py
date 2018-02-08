from django.shortcuts import (
    render,
    redirect)
from django.urls import reverse
from .models import (
    Play,
    Review,
    )
from .forms import (
    PlayForm,
    ReviewForm
    )
# Create your views here.


def search(request):
    form = PlayForm()
    box = Play.objects.order_by('grade')
    ctx = {
        'form': form,
        'box': box
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
    ctx = {
        'play': play
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


def review_create(request, playid):
    print(request.POST)
    form = ReviewForm(request.POST or None)
    print(form)
    play = Play.objects.get(playid=playid)
    if request.method == 'POST' and form.is_valid():
        print(request.POST['rate'])
        review = form.save(commit=False)
        review.rate = request.POST.get('rate')
        review.author = request.user
        review.play = Play.objects.get(playid=playid)
        review.save()
        return redirect(reverse(
            'search:review',
            kwargs={'playid': review.play.playid}
            ))
    ctx = {
        'form': form,
        'play': play
    }
    return render(request, 'review_create.html', ctx)


def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    ctx = {
        'review': review
    }
    return render(request, 'review_detail.html', ctx)
