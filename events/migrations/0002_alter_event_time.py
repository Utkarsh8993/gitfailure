# Generated by Django 4.1.5 on 2023-01-14 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 14, 17, 51, 53, 95074)),
        ),
    ]
