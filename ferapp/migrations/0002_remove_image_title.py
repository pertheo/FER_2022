# Generated by Django 4.0.4 on 2022-06-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
    ]
