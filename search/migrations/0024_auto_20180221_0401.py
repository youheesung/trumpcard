# Generated by Django 2.0.1 on 2018-02-20 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0023_review_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag_comment', to='search.Tag'),
        ),
    ]
