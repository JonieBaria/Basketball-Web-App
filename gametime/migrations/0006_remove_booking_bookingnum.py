# Generated by Django 4.0.6 on 2022-07-27 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0005_booking_bookingnum_alter_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bookingnum',
        ),
    ]
