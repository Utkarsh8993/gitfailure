# Generated by Django 4.1.5 on 2023-01-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0003_delete_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
