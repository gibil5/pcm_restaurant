# Generated by Django 2.2.6 on 2019-10-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0040_auto_20191031_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
    ]
