# Generated by Django 2.0.1 on 2018-02-03 09:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20180203_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content Of Post'),
        ),
    ]