# Generated by Django 4.1.3 on 2022-12-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomservice', '0007_alter_roomservice_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomserviceorder',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
