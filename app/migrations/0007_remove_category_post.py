# Generated by Django 3.0.7 on 2020-06-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200607_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
    ]
