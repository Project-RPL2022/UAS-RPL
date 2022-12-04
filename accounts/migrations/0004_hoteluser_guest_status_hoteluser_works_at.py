# Generated by Django 4.1.3 on 2022-11-29 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
        ('accounts', '0003_alter_hoteluser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteluser',
            name='guest_status',
            field=models.CharField(choices=[('CHECK-IN', 'CHECK-IN'), ('CHECK-OUT', 'CHECK-OUT')], default='CHECK-OUT', max_length=30),
        ),
        migrations.AddField(
            model_name='hoteluser',
            name='works_at',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel'),
        ),
    ]
