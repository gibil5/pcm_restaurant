# Generated by Django 2.2.6 on 2019-11-08 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20191108_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ('idx',), 'verbose_name': 'Familia', 'verbose_name_plural': 'Familias'},
        ),
    ]
