# Generated by Django 3.1 on 2020-08-23 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('accomodation_type', models.CharField(max_length=100)),
                ('start_hour', models.CharField(max_length=100)),
                ('end_hour', models.CharField(max_length=100)),
                ('lat_1', models.FloatField()),
                ('long_1', models.FloatField()),
                ('lat_2', models.FloatField()),
                ('long_2', models.FloatField()),
                ('stars', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='mydb_data_layer.address')),
            ],
        ),
    ]
