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



class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    image = models.ImageField(
        upload_to='profile/%Y/%m/%d',
        blank=True,
        null=True,
        )
    birth_date = models.DateField(
        null=True,
        blank=True)

    liebe_t = models.CharField(
        blank=True,
        null=True,
        verbose_name='당신의 가장 좋아하는 연극 하나만!! 알려주세욯ㅎ??',
        max_length=30,
        )
    liebe_a = models.CharField(
        blank=True,
        null=True,
        verbose_name='좋아하는 배우는요? 딱 한사람만 말하셔야 되용ㅎㅎ 프로그램을 그따구로 해서 ㅋㅋㅋ',
        max_length=100
        )

    price = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='선호가격'
        )
    recommand_t = models.CharField(
        blank=True,
        null=True,
        verbose_name='짧은 자기 소개!',
        max_length=100,
        )

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_profile_image.jpg'
        return image_url

    group_image = models.ImageField(
        upload_to='profile/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name='극단사진 giveme',
        )

    is_groupuser = models.BooleanField(
        default=False
        )

    follow = models.ManyToManyField(
        "self",
        related_name='follower',
        blank=True,
        null=True,
        symmetrical=False
        )


    genre_select = MultiSelectField(
        max_length=250,
        blank=True,
        null=True,
        choices=gerne_name,
        verbose_name='극의 장르 '
    )

    play_char = MultiSelectField(
            max_length=250,
            blank=True,
            null=True,
            choices=character,
            verbose_name='극의 특징',
            )

    def __str__(self):
        return '{0}'.format(self.user.username)

    def group_image_url(self):
        if self.group_image:
            group_image_url = self.image.url
        else:
            group_image_url = '/static/img/default_profile_image.jpg'
        return group_image_url