# Generated by Django 4.0.4 on 2022-05-27 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaloffice', '0004_remove_user_test_alter_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 58, 36, 674364)),
        ),
        migrations.AlterField(
            model_name='user',
            name='beginDate',
            field=models.DateField(blank=True),
        ),
    ]