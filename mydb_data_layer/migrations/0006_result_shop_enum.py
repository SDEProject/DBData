# Generated by Django 3.1 on 2020-09-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydb_data_layer', '0005_auto_20200901_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='shop_enum',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
