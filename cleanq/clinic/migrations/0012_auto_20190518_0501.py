# Generated by Django 2.2.1 on 2019-05-18 05:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0011_auto_20190518_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 18, 8, 1, 19, 543065, tzinfo=utc), verbose_name='end time'),
        ),
    ]
