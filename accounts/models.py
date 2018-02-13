from django.db import models
from django.conf import settings
# Create your models here.

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
    birth_date = models.DateField(blank=True)
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

class GroupProfile(models.Model):
    groupuser = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    group_image = models.ImageField(
        upload_to='profile/%Y/%m/%d',
        blank=True,
        null=True,
        verbose_name='극단사진 giveme',
        )

    is_groupuser = models.BooleanField(
        default=True,
        )


    def group_image_url(self):
        if self.group_image:
            group_image_url = self.image.url
        else:
            group_image_url = '/static/img/delfault_group_image.jpg'