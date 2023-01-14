# Generated by Django 4.1.5 on 2023-01-13 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_remove_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('branch', models.CharField(choices=[('ME', 'Mechanical Engineering'), ('CSE', 'Computer Science Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('EE', 'Electrical Engineering'), ('EPH', 'Engineering Physics'), ('NON', 'others or None of the Above')], max_length=3)),
                ('enrolno', models.CharField(max_length=8)),
                ('votes', models.IntegerField(default=0)),
                ('voted_for', models.BooleanField(default=False)),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('vote_1_bool', models.BooleanField(default=False)),
                ('vote_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to='elections.candidate')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
            managers=[
                ('objects', users.manager.UserManager()),
            ],
        ),
    ]
