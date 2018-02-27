from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField


# Create your models here.
gerne_name = (
        (1, '비극 '),
        (2, '희극 '),
        (3, '비희극 '),
        (4, '소극 '),
        (5, '통속극 '),
        (6, '공포 '),
        (7, '스릴러 '),
        (8, '추리극 '),
        (9, '로맨틱 '),
        )

character = (
        (1, '예술적'),
        (2, '실험적'),
        (3, '대중적'),
        (4, 'NTLIVE/해외생중계공연'),
        (5, '감동적'),
        (6, '웃음만발'),
        (7, '아이와 함께'),
        (8, '어머! 눈감아'),
        )


class Play(models.Model):
    to_my_heart = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name='play_to_my_heart',
        )

    playid = models.CharField(
        max_length=15,
        verbose_name='연극ID')
    placeid = models.CharField(
        null=True,
        max_length=15,
        verbose_name='공연장소ID')
    name = models.CharField(
        max_length=20,
        verbose_name='제목')
    start_date = models.DateField(
        verbose_name='시작일')
    end_date = models.DateField(
        verbose_name='종료일')
    place = models.CharField(
        max_length=20,
        verbose_name='장소')
    actor = models.CharField(
        max_length=60,
        verbose_name='배우')
    staff = models.CharField(
        null=True,
        max_length=60,
        verbose_name='제작')
    runtime = models.CharField(
        max_length=10,
        verbose_name='런타임')
    poster = models.URLField(
        null=True,
        blank=True,
        verbose_name='포스터이미지경로')
    styurl1 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='소개이미지1')
    styurl2 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='소개이미지2')
    styurl3 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='소개이미지3')
    styurl4 = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='소개이미지4')
    price = models.CharField(
        max_length=10,
        verbose_name='가격')
    time = models.CharField(
        max_length=80,
        verbose_name='공연시간')
    minprice = models.IntegerField(
        default=1,
        verbose_name='최소가격')

    grade = models.IntegerField(
        default=0,
        null=True,
        verbose_name='순위',
        )

    rate = models.DecimalField(
        max_digits=10,
        decimal_places=1,
        default=0,
        verbose_name='평점'
        )

    genre_select = MultiSelectField(
        max_length=250,
        blank=True,
        null=True,
        choices=gerne_name,
        verbose_name='극의 장르 '
        )

    Text_base = models.BooleanField(
        default=False,
        verbose_name='희곡 기반',
        )

    play_char = MultiSelectField(
        max_length=250,
        blank=True,
        null=True,
        choices=character,
        verbose_name='극의 특징',
        )

    theater = models.ForeignKey(
        'Theater',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='극장'
        )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )

    poster_self = models.ImageField(
        upload_to='poster/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name='포스터이미지')
    styurl1_self = models.ImageField(
        upload_to='styurl1/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='이미지1')
    styurl2_self = models.ImageField(
        upload_to='styurl2/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='이미지2')
    styurl3_self = models.ImageField(
        upload_to='styurl3/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='이미지3')
    styurl4_self = models.ImageField(
        upload_to='styurl4/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='이미지4')

    confirmed = models.BooleanField(
        default=False,
        verbose_name='검증')

    user_upload = models.BooleanField(
        default=False,
        verbose_name='유저입력')

    lat = models.FloatField(
        null=True,
        blank=True,
        verbose_name='위도'
        )

    lng = models.FloatField(
        null=True,
        blank=True,
        verbose_name='경도'
        )


    def __str__(self):
        return '{0}'.format(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Review(models.Model):
    play = models.ForeignKey(
        Play,
        on_delete=models.CASCADE
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='author'
        )
    title = models.CharField(
        max_length=30,
        verbose_name='제목')
    content = models.TextField()

    rate = models.IntegerField(
        default=0,
        verbose_name='평점'
        )

    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='tag_comment',
        )

    img1 = models.ImageField(
        upload_to='reviewimg/{0}/'.format(play.name),
        null=True,
        blank=True,
        verbose_name='이미지1'
        )
    img2 = models.ImageField(
        upload_to='reviewimg/{0}/'.format(play.name),
        null=True,
        blank=True,
        verbose_name='이미지2'
        )
    img3 = models.ImageField(
        upload_to='reviewimg/{0}/'.format(play.name),
        null=True,
        blank=True,
        verbose_name='이미지3'
        )
    img4 = models.ImageField(
        upload_to='reviewimg/{0}/'.format(play.name),
        null=True,
        blank=True,
        verbose_name='이미지4'
        )

class Theater(models.Model):
    placeid = models.CharField(
        max_length=15,
        verbose_name='공연장ID')
    name = models.CharField(
        max_length=30,
        verbose_name='공연장이름')
    theater_count = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='공연장수')
    tel = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='전화번호')
    page = models.URLField(
        null=True,
        blank=True)
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='주소')
    latitude = models.FloatField(
        null=True,
        blank=True)
    longitude = models.FloatField(
        null=True,
        blank=True)

    def __str__(self):
        return '{0}'.format(self.name)
