# Generated by Django 2.2.6 on 2019-10-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0024_auto_20191030_1950'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Drinks',
            new_name='Drink',
        ),
        migrations.RenameModel(
            old_name='HotDrinks',
            new_name='HotDrink',
        ),
    ]
