# Generated by Django 2.2.6 on 2019-11-07 01:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0062_auto_20191106_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha'),
        ),
    ]
