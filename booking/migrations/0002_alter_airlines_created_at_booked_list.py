# Generated by Django 5.1.4 on 2024-12-25 07:28

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airlines',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 25, 13, 13, 18, 982942)),
        ),
        migrations.CreateModel(
            name='Booked_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=200)),
                ('passenger_age', models.IntegerField()),
                ('book_date', models.DateTimeField()),
                ('book_time', models.DateTimeField()),
                ('Airlines_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.airlines')),
            ],
        ),
    ]
