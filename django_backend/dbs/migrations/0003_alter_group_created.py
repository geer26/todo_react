# Generated by Django 4.1.2 on 2022-10-12 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0002_group_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 12, 7, 16, 0, 121964, tzinfo=datetime.timezone.utc)),
        ),
    ]
