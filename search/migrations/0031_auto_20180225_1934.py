# Generated by Django 2.0.1 on 2018-02-25 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0030_auto_20180225_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='reviewimg/None/', verbose_name='이미지1'),
        ),
        migrations.AddField(
            model_name='review',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='reviewimg/None/', verbose_name='이미지2'),
        ),
        migrations.AddField(
            model_name='review',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='reviewimg/None/', verbose_name='이미지3'),
        ),
        migrations.AddField(
            model_name='review',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to='reviewimg/None/', verbose_name='이미지4'),
        ),
    ]
