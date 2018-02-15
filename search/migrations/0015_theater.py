# Generated by Django 2.0.1 on 2018-02-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0014_auto_20180211_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeid', models.CharField(max_length=15, verbose_name='공연장ID')),
                ('name', models.CharField(max_length=30, verbose_name='공연장이름')),
                ('theater_count', models.IntegerField(blank=True, null=True, verbose_name='공연장수')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='전화번호')),
                ('page', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='주소')),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
