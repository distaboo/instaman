# Generated by Django 2.0.5 on 2019-01-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190108_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='postsPerDay',
            field=models.IntegerField(default=3),
        ),
    ]