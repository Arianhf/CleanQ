# Generated by Django 2.2.1 on 2019-05-16 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_auto_20190516_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 16, 20, 54, 38, 762143, tzinfo=utc), verbose_name='end time'),
        ),
    ]
