# Generated by Django 2.2.1 on 2019-05-16 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicrepresentative',
            name='user',
            field=models.ForeignKey(help_text='user of the representative', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='clinic',
            name='rep',
            field=models.ForeignKey(help_text='representative of the clinic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.ClinicRepresentative', verbose_name='rep'),
        ),
        migrations.AddField(
            model_name='basicuser',
            name='user',
            field=models.ForeignKey(help_text='user of the basic user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
