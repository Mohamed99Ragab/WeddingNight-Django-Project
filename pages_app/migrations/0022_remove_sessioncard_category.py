# Generated by Django 4.0.3 on 2022-06-13 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0021_sessioncard_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessioncard',
            name='category',
        ),
    ]
