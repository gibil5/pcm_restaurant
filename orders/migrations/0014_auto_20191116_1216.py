# Generated by Django 2.2.6 on 2019-11-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20191116_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='qty',
            field=models.PositiveIntegerField(verbose_name='cantidad'),
        ),
    ]
