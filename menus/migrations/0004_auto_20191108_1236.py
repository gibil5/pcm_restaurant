# Generated by Django 2.2.6 on 2019-11-08 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_auto_20191108_1229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('-date',), 'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
    ]
