# Generated by Django 3.0.7 on 2020-11-19 18:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_auto_20201119_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('date_visited', models.DateTimeField(default=datetime.datetime(2020, 11, 19, 18, 6, 3, 954871, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_visited',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 18, 6, 3, 724674, tzinfo=utc)),
        ),
    ]
