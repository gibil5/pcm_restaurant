# Generated by Django 2.2.6 on 2019-11-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_cook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_waiter',
            field=models.BooleanField(default=False),
        ),
    ]
