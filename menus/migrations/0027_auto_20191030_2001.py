# Generated by Django 2.2.6 on 2019-10-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0026_auto_20191030_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='family',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]