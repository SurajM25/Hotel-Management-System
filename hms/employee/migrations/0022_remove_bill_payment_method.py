# Generated by Django 3.0.7 on 2020-11-28 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0021_auto_20201127_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='payment_method',
        ),
    ]
