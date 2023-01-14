# Generated by Django 4.1.5 on 2023-01-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_event_manager_alter_event_date_and_more'),
        ('users', '0008_remove_user_vote_1_remove_user_vote_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='user', to='events.event'),
        ),
        migrations.AddField(
            model_name='user',
            name='organised_events',
            field=models.ManyToManyField(blank=True, related_name='manager', to='events.event'),
        ),
    ]