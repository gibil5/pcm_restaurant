# Generated by Django 2.2.6 on 2019-10-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0035_remove_family_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]