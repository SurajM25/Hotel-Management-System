# Generated by Django 3.0.7 on 2020-11-21 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_auto_20201120_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_visited',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 14, 35, 57, 323600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customerlog',
            name='date_visited',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 14, 35, 57, 543013, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uses',
            name='time_used',
            field=models.TimeField(default=datetime.datetime(2020, 11, 21, 14, 35, 57, 547002, tzinfo=utc)),
        ),
    ]
