# Generated by Django 3.0.8 on 2020-07-15 06:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200714_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='duedate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 15, 12, 5, 29, 471900)),
        ),
    ]