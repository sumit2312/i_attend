# Generated by Django 2.2.4 on 2019-09-02 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date_added',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 9, 2, 20, 4, 6, 322072)),
        ),
    ]
