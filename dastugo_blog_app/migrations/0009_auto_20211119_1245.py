# Generated by Django 3.2.9 on 2021-11-19 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dastugo_blog_app', '0008_auto_20211119_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 19, 12, 45, 21, 580061)),
        ),
    ]