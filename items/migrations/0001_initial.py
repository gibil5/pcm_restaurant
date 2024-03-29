# Generated by Django 2.2.6 on 2019-11-07 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Familia',
                'verbose_name_plural': 'Familias',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nombre')),
                ('price', models.FloatField(default=0)),
                ('family', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='items.Family')),
            ],
            options={
                'verbose_name': 'Plato',
                'verbose_name_plural': 'Platos',
                'ordering': ('family',),
            },
        ),
    ]
