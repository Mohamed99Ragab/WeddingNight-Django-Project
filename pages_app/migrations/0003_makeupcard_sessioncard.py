# Generated by Django 4.0.3 on 2022-06-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0002_hallcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakeupCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_session', models.ImageField(blank=True, null=True, upload_to='makeup')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='SessionCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_session', models.ImageField(blank=True, null=True, upload_to='session')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
