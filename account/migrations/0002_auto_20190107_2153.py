# Generated by Django 2.0.5 on 2019-01-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='followPerDay',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='account',
            name='photoDescription',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='account',
            name='target',
            field=models.CharField(max_length=1000),
        ),
    ]
