# Generated by Django 2.2.6 on 2019-11-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20191120_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='state',
            field=models.CharField(choices=[('Inicio', 'Inicio'), ('Preparación', 'En preparacion'), ('Listo', 'Listo'), ('Servido', 'Servido'), ('Pagado', 'Pagado'), ('Cancelado', 'Cancelado')], default='Inicio', max_length=100),
        ),
    ]
