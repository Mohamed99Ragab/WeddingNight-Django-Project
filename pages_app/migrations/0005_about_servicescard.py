# Generated by Django 4.0.3 on 2022-06-10 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0004_rename_photo_session_makeupcard_photo_makeup'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_about', models.ImageField(blank=True, null=True, upload_to='about')),
                ('heading_hero', models.CharField(max_length=250)),
                ('title_hero', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicesCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_services', models.ImageField(blank=True, null=True, upload_to='services')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
