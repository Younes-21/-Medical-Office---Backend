# Generated by Django 4.0.4 on 2022-05-27 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaloffice', '0002_alter_appointment_date_alter_appointment_reason_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 48, 51, 642884)),
        ),
    ]
