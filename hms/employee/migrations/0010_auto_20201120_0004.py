# Generated by Django 3.0.7 on 2020-11-19 18:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20201119_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_visited',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 18, 34, 11, 880512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customerlog',
            name='date_visited',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 18, 34, 12, 105175, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Uses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_used', models.TimeField(default=datetime.datetime(2020, 11, 19, 18, 34, 12, 113255, tzinfo=utc))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.CustomerLog')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Services')),
            ],
        ),
    ]
