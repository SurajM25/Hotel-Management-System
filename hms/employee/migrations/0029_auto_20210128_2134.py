# Generated by Django 2.2.10 on 2021-01-28 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0028_customer_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='customer',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.CustomerLog'),
        ),
    ]