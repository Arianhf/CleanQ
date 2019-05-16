# Generated by Django 2.2.1 on 2019-05-16 17:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20190516_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='clinic',
            field=models.ForeignKey(help_text='the clinic that this time slot belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='clinic', to='clinic.Clinic', verbose_name='clinic'),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 16, 20, 11, 32, 135121, tzinfo=utc), verbose_name='end time'),
        ),
    ]
