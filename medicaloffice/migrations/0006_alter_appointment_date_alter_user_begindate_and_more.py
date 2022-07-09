# Generated by Django 4.0.4 on 2022-05-27 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaloffice', '0005_alter_appointment_date_alter_user_begindate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 16, 6, 15, 551130)),
        ),
        migrations.AlterField(
            model_name='user',
            name='beginDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]