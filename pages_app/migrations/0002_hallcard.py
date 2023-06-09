# Generated by Django 4.0.3 on 2022-06-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HallCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_hall', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
