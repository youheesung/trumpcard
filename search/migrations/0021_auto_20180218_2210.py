# Generated by Django 2.0.1 on 2018-02-18 13:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0020_play_tomyheart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='play',
            name='tomyheart',
        ),
        migrations.AddField(
            model_name='play',
            name='to_my_heart',
            field=models.ManyToManyField(related_name='play_to_my_heart', to=settings.AUTH_USER_MODEL),
        ),
    ]
