# Generated by Django 2.0.1 on 2018-02-04 01:55

from django.db import migrations
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20180204_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=django_summernote.fields.SummernoteTextField(default=''),
        ),
    ]
