# Generated by Django 2.2.6 on 2019-10-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0023_auto_20191030_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='drinks',
            field=models.ManyToManyField(blank=True, to='menus.Drinks'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='hot_drinks',
            field=models.ManyToManyField(blank=True, to='menus.HotDrinks'),
        ),
    ]