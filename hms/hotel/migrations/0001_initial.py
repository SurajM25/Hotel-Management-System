# Generated by Django 3.0.7 on 2020-11-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='onlinebooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('room_type', models.CharField(max_length=10)),
                ('booking_date', models.DateField()),
            ],
        ),
    ]
