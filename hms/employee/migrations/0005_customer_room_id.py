# Generated by Django 3.0.7 on 2020-11-19 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_room_occupied_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='room_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.Room'),
        ),
    ]
