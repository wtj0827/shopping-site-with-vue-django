# Generated by Django 3.0.1 on 2020-01-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20200105_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='businessYear',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
