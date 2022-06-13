# Generated by Django 4.0.3 on 2022-06-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0014_sessioncard_photographer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessioncard',
            name='Photography_Cost',
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='Administrator',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='TimeToAppointment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='book_url',
            field=models.URLField(blank=True, default='http://127.0.0.1:8000/contact/', null=True),
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='makeupcard',
            name='service_provide',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='makeupcard',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='sessioncard',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
