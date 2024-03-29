# Generated by Django 2.2.6 on 2019-11-13 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cook',
            field=models.ForeignKey(limit_choices_to={'is_cook': True}, on_delete=django.db.models.deletion.PROTECT, related_name='cook', to='employees.Employee'),
        ),
        migrations.AlterField(
            model_name='order',
            name='waiter',
            field=models.ForeignKey(limit_choices_to={'is_waiter': True}, on_delete=django.db.models.deletion.PROTECT, related_name='waiter', to='employees.Employee'),
        ),
    ]
