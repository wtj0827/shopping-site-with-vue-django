# Generated by Django 3.0.1 on 2020-01-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_auto_20191226_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(help_text='Enter factory name', max_length=200, null=True),
        ),
    ]
