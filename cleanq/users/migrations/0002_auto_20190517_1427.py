# Generated by Django 2.2.1 on 2019-05-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_basic',
            field=models.BooleanField(default=True, verbose_name='basic status'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_rep',
            field=models.BooleanField(default=False, verbose_name='rep status'),
        ),
    ]
