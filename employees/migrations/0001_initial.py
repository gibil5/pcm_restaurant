# Generated by Django 2.2.6 on 2019-11-11 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='nombre')),
                ('idx', models.IntegerField(default=0, verbose_name='orden')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ('idx',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='nombre')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='descripción')),
                ('image', models.CharField(default='https://res.cloudinary.com/dam0dmleq/image/upload/v1573501278/pcm/empty_black.png', max_length=200, verbose_name='imagen')),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='employees.Category')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ('name',),
            },
        ),
    ]
