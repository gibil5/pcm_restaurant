# Generated by Django 2.2.6 on 2019-11-07 01:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0056_auto_20191106_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 6, 20, 40, 9, 366925), verbose_name='fecha'),
        ),
    ]
