# Generated by Django 2.0.1 on 2018-02-12 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_image', models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d', verbose_name='극단사진 giveme')),
                ('is_groupuser', models.BooleanField(default=True)),
                ('groupuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d')),
                ('birth_date', models.DateField(blank=True)),
                ('liebe_t', models.CharField(blank=True, max_length=30, null=True, verbose_name='당신의 가장 좋아하는 연극 하나만!! 알려주세욯ㅎ??')),
                ('liebe_a', models.CharField(blank=True, max_length=100, null=True, verbose_name='좋아하는 배우는요? 딱 한사람만 말하셔야 되용ㅎㅎ 프로그램을 그따구로 해서 ㅋㅋㅋ')),
                ('recommand_t', models.CharField(blank=True, max_length=100, null=True, verbose_name='짧은 자기 소개!')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
