# Generated by Django 2.2.10 on 2021-01-28 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0033_auto_20210128_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uses',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.CustomerLog'),
        ),
    ]
