# Generated by Django 2.2.6 on 2019-11-19 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_delete_category'),
        ('orders', '0017_auto_20191116_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cook',
            field=models.ForeignKey(blank=True, default=1, limit_choices_to={'is_cook': True}, on_delete=django.db.models.deletion.PROTECT, related_name='cook', to='employees.Employee', verbose_name='cocinero'),
            preserve_default=False,
        ),
    ]
