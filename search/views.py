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


def counter(a, b, c):
    count = c
    for i in a:
        if i in b:
            count += 1
    return count

def search(request):
    form = PlayForm()
    box = Play.objects.order_by('grade')
    ctx = {
        'form': form,
        'box': box,
    }
    if request.user.is_authenticated:
        recommend1 = Play.objects.all()
        recommend2 = Play.objects.all()
        gen = list(request.user.profile.genre_select)
        char = list(request.user.profile.play_char)
        print(gen)
        print(char)
        recommend = Play.objects.none()
        for i in range(1, 10):
            if str(i) in gen:
                print('\'{0}\''.format(str(i)))
                print(str(i) in gen)
                recommend = recommend | recommend1.filter(genre_select__contains=str(i))
        for i in range(1, 9):
            if str(i) in char:
                print('\'{0}\''.format(str(i)))
                print(str(i) in char)
                recommend = recommend | recommend.filter(play_char__contains=str(i))
        count = {}
        for i in recommend:
            count[i] = counter(gen, i.genre_select, 0)
            print('%s: %d' % (i.name, count[i]))
        for i in recommend:
            count[i] = counter(char, i.play_char, count[i])
            print('%s: %d' % (i.name, count[i]))
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        counted = []
        for i in count:
            counted.append(i[0])
        print(counted)
        # count.sort(key=lambda x: x[1], reverse=True)

        # recommend = recommend1 & recommend2
        # recommend1 = recommend1.extra(select={'length': 'Length(genre_select)'}).order_by('-length')
        # for i in recommend:
        #     print(i.name)
        #     print(i.genre_select)
        #     print(i.play_char)
        #     print('\n')
        ctx['recommend'] = counted
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
    review = Review.objects.filter(play__playid=playid)
    ctx = {
        'play': play,
        'theater': theater,
        'review': review,
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
            new_review.tag.set(request.POST.getlist('tag[]'))
            print(new_review.tag.first())
            review = Review.objects.filter(play__playid=playid)
            review_count = review.count()
            rateSum = 0
            for i in review:
                rateSum += i.rate
            rateSum /= review_count
            play.update(rate=rateSum)
            # return redirect(reverse('search:review_detail', kwargs={'pk':new_review.pk}))
    ctx = {
        'form': form,
        'play': play.get(playid=playid)
    }
    return render(request, 'review_create.html', ctx)

##
def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    review_tag = review.tag.all()

    ctx = {
        'review': review,
        'review_tag':review_tag,
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


def recommend(request):
    return render(request, 'cardnews.html')
