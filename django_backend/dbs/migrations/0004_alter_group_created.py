# Generated by Django 4.1.2 on 2022-10-12 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0003_alter_group_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]