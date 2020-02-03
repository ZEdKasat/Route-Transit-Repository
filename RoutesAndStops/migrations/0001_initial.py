# Generated by Django 3.0.2 on 2020-02-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route Name')),
                ('direction', models.BooleanField(choices=[(True, 'UP'), (False, 'Down')], verbose_name='Direction')),
                ('status', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], verbose_name='Status')),
                ('list_of_stops', models.TextField(verbose_name='Stops')),
                ('type', models.BooleanField(choices=[(True, 'AC'), (False, 'General')], verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('latitudes', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitudes')),
                ('longitudes', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitudes')),
            ],
        ),
    ]
