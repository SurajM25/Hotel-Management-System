# Generated by Django 3.0.7 on 2020-11-20 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('phoneno', models.IntegerField()),
                ('emailid', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('designation', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('aadharno', models.CharField(max_length=15)),
                ('datejoined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
