# Generated by Django 2.0.1 on 2018-02-19 09:54

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180219_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='genre_select',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '비극 '), (2, '희극 '), (3, '비희극 '), (4, '소극 '), (5, '통속극 '), (6, '공포 '), (7, '스릴러 '), (8, '추리극 '), (9, '로맨틱 ')], max_length=250, null=True, verbose_name='극의 장르 '),
        ),
        migrations.AddField(
            model_name='profile',
            name='play_char',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '예술적'), (2, '실험적'), (3, '대중적'), (4, 'NTLIVE/해외생중계공연'), (5, '감동적'), (6, '웃음만발'), (7, '아이와 함께'), (8, '어머! 눈감아')], max_length=250, null=True, verbose_name='극의 특징'),
        ),
    ]
