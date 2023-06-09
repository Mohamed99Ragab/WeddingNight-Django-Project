# Generated by Django 4.0.3 on 2022-06-13 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages_app', '0016_hallcard_category_makeupcard_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hallcard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages_app.categories'),
        ),
        migrations.AlterField(
            model_name='makeupcard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages_app.categories'),
        ),
        migrations.AlterField(
            model_name='sessioncard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages_app.categories'),
        ),
    ]
