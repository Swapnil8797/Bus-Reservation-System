# Generated by Django 3.2.7 on 2021-12-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20211228_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='date_r'),
        ),
    ]