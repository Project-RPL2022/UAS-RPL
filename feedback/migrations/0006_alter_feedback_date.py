# Generated by Django 4.1.3 on 2022-12-03 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_alter_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 22, 47, 49, 38291)),
        ),
    ]
