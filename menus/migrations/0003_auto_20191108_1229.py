# Generated by Django 2.2.6 on 2019-11-08 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_remove_menu_family_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='fecha'),
        ),
    ]
