# Generated by Django 3.0.1 on 2020-01-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='birthday',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='businessYear',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
