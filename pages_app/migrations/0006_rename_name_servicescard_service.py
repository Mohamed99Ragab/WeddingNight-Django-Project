# Generated by Django 4.0.3 on 2022-06-10 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0005_about_servicescard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicescard',
            old_name='name',
            new_name='service',
        ),
    ]
