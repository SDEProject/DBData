# Generated by Django 3.1 on 2020-08-24 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydb_data_layer', '0003_auto_20200824_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='accommodation_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='end_hour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='lat_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='lat_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='long_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='long_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='stars',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='start_hour',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
