# Generated by Django 2.2.6 on 2019-11-07 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(blank=True, max_length=200, verbose_name='imágen'),
        ),
    ]
