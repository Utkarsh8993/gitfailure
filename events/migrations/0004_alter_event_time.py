# Generated by Django 4.1.5 on 2023-01-14 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 14, 22, 26, 3, 657991)),
        ),
    ]