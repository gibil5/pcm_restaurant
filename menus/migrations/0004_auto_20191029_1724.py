# Generated by Django 2.2.6 on 2019-10-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20191029_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='menus',
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(to='menus.Item'),
        ),
    ]
