# Generated by Django 2.0.1 on 2018-02-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0026_play_theater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='styurl1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='소개이미지1'),
        ),
        migrations.AlterField(
            model_name='play',
            name='styurl2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='소개이미지2'),
        ),
        migrations.AlterField(
            model_name='play',
            name='styurl3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='소개이미지3'),
        ),
        migrations.AlterField(
            model_name='play',
            name='styurl4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='소개이미지4'),
        ),
    ]
