# Generated by Django 2.2.6 on 2019-10-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0031_auto_20191030_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='name',
            field=models.CharField(blank=True, choices=[('entry', 'Entry'), ('main_course', 'Main Course')], max_length=100),
        ),
    ]
