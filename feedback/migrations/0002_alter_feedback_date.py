# Generated by Django 3.2.8 on 2022-12-03 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 18, 52, 17, 7116)),
        ),
    ]
