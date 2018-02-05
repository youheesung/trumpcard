from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
    image = models.ImageField(
        upload_to = 'profile/%Y/%m/%d',
        blank=True,
        null=True,
        )
    birth_date = models.DateField(blank=True)
    liebe_t = models.TextField(blank=True, null=True)
    liebe_a = models.TextField(blank=True, null=True)

    recommand_t = models.TextField(blank=True, null=True)

    def image_url(self):
        if self.image:
            image_url = self.image.url
        else:
            image_url = '/static/img/default_profile_image.jpg'
