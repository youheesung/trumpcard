from django.shortcuts import (
    render,
    redirect)
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import (
    Play,
    Review,
    Theater
    )
from .forms import (
    CreatePlayForm,
    ReviewForm
    )

from django.http import HttpResponse
import re
# Create your views here.


def counter(a, b, c):
    count = c
    for i in a:
        if i in b:
            count += 1
    return count

def hangul(s):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
    #hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  #위와 동일
    result = hangul.sub('', s) #한글과 띄어쓰기를 제외한 모든 부분을 제거
    result = result.split(' ')
    print (result)
    return result


def search(request):
    box = Play.objects.order_by('grade')
    rate = Play.objects.order_by('-rate')
    play = Play.objects.all()

    ## 리뷰의 갯수 순으로 뽑아내기
    review_count_b = []
    review_count = {}
    for j in play:
        review_count_b.append(j)
    for p in review_count_b:
        review_count[p] = p.review_set.count()

    count = sorted(review_count.items(), key=lambda x: x[1], reverse=True)

    counted = []
    for v in count:
        counted.append(v[0])
    print_review_count = counted[0:11]
    ## count의 수로 나눈다??

    ## 별점 순으로 뽑아내기
    review_rate = []
    for i in rate:
        if(i.rate is not None):
            review_rate.append(i)
    print_rate = review_rate[0:11]

    ctx = {
        'rate': print_rate,
        'box': box,
        'review_count': print_review_count,
    }
    if request.user.is_authenticated:
        recommend1 = Play.objects.all()
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
        for i in range(1, 10):
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


@login_required
def detail(request, playid):
    play = Play.objects.get(playid=playid)
    review = Review.objects.filter(play__playid=playid)
    ##rate

    review_tag =[]
    for i in review:
        review_tag.append(i.tag)

    ctx = {
        'play': play,
        'review': review,
        'review_tag':review_tag,
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

@login_required
def review_create(request, playid):

    form = ReviewForm()
    play = Play.objects.filter(playid=playid)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_review = form.save(commit=False)
            print(request.POST)
            new_review.author = request.user
            new_review.play = play.get(playid=playid)

            new_review.save()
            new_review.tag.set(request.POST.getlist('tag'))
            review = Review.objects.filter(play__playid=playid)
            review_count = review.count()
            rateSum = 0
            for i in review:
                rateSum += i.rate
            rateSum /= review_count
            play.update(rate=rateSum)
            # return redirect(reverse('search:review_detail', kwargs={'pk':new_review.pk}))
            return redirect(reverse('search:detail', kwargs={'playid': play.first().playid}))
    ctx = {
        'form': form,
        'play': play.get(playid=playid)
    }
    return render(request, 'review_create.html', ctx)


def review_update(request, pk):
    review = Review.objects.get(pk=pk)
    form = ReviewForm(instance=review)
    play = Play.objects.filter(playid=review.play.playid)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES or None, instance=review)
        if form.is_valid():
            new_review = form.save(commit=False)
            print(request.POST)
            new_review.author = request.user
            new_review.play = play.get(playid=review.play.playid)

            new_review.save()
            new_review.tag.set(request.POST.getlist('tag'))
            review = Review.objects.filter(play__playid=review.play.playid)
            review_count = review.count()
            rateSum = 0
            for i in review:
                rateSum += i.rate
            rateSum /= review_count
            play.update(rate=rateSum)
            # return redirect(reverse('search:review_detail', kwargs={'pk':new_review.pk}))
            return redirect(reverse('search:detail', kwargs={'playid': play.first().playid}))
    ctx = {
        'form': form,
        'play': play.get(playid=review.play.playid)
    }
    return render(request, 'review_create.html', ctx)


@login_required
def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    review_tag = review.tag.all()
    # box = Play.objects.order_by('grade')

    ctx = {
        'review': review,
        'review_tag':review_tag,
    }
    return render(request, 'review_detail.html', ctx)


@login_required
def play_create(request, username):
    author = request.user
    form = CreatePlayForm(request.POST or None, request.FILES or None)
    genre = request.POST.getlist('genre_select[]')
    char = request.POST.getlist('play_char[]')
    if request.method == "POST" and form.is_valid():
        play = form.save(commit=False)
        id = Play.objects.last().playid
        str_id = 'PF{0}'.format(int(id[-6:])+1)
        play.playid = str_id
        play.genre_select = genre
        play.play_char = char
        play.user_upload = True
        play.author = author
        play.save()
        return redirect(reverse('search:detail', kwargs={'playid': play.playid}))
    ctx = {
        'form': form,
    }
    return render(request, 'play_create.html', ctx)


@login_required
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


def cardnews(request):
    return render(request, 'cardnews.html')


@login_required
def recommend(request):
    recommend1 = Play.objects.all()
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
    for i in range(1, 10):
        if str(i) in char:
            print('\'{0}\''.format(str(i)))
            print(str(i) in char)
            recommend = recommend | recommend1.filter(play_char__contains=str(i))
            print(recommend)
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

    price = request.user.profile.price
    if price is not None:
        recommend_price = Play.objects.filter(minprice__lte=price)
    else:
        recommend_price = Play.objects.none()

    recommend_actor = Play.objects.none()
    recommend_staff = Play.objects.none()
    actor = request.user.profile.liebe_a
    print(actor)
    if actor is not None:
        if len(actor) >= 3:
            actor = hangul(actor)
            for i in actor:
                if Play.objects.filter(actor__contains=i).exists():
                    recommend_actor |= Play.objects.filter(actor__contains=i)

    staff = request.user.profile.liebe_t
    print(staff)
    if staff is not None:
        if len(staff) >= 3:
            staff = hangul(staff)
            for i in staff:
                if Play.objects.filter(staff__contains=i).exists():
                    recommend_staff |= Play.objects.filter(staff__contains=i)


    ctx = {
        'recommend': counted,
        'recommend_price': recommend_price,
        'recommend_actor': recommend_actor,
        'recommend_staff': recommend_staff,
    }
    return render(request, 'recommend.html', ctx)