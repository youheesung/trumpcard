# Generated by Django 2.0.1 on 2018-02-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180215_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(default=1, related_name='_profile_follow_+', to='accounts.Profile'),
        ),
    ]
