# Generated by Django 5.0.1 on 2024-01-23 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_activation_expires_at_alter_activation_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 18, 31, 56, 234828, tzinfo=datetime.timezone.utc)),
        ),
    ]
