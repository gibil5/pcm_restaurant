# Generated by Django 2.2.6 on 2019-11-05 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20191105_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
    ]
