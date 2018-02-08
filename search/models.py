from django.db import models
from django.conf import settings



# Create your models here.
class Play(models.Model):
    playid = models.CharField(
        max_length=15,
        verbose_name='연극ID')
    placeid = models.CharField(
        null=True,
        max_length=15,
        verbose_name='공연장소ID')
    name = models.CharField(
        max_length=20,
        verbose_name='이름')
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
        verbose_name='포스터이미지경로')
    styurl1 = models.CharField(
        max_length=100,
        verbose_name='소개이미지1')
    styurl2 = models.CharField(
        max_length=100,
        verbose_name='소개이미지2')
    styurl3 = models.CharField(
        max_length=100,
        verbose_name='소개이미지3')
    styurl4 = models.CharField(
        max_length=100,
        null=True,
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
        decimal_places=9,
        default=0,
        verbose_name='평점'
        )

    def __str__(self):
        return '{0}'.format(self.name)


class Review(models.Model):
    play = models.ForeignKey(
        Play,
        on_delete=models.CASCADE
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    title = models.CharField(
        max_length=30,
        verbose_name='제목')
    content = models.TextField()

    rate = models.IntegerField(
        default=0,
        verbose_name='평점'
        )
