# Generated by Django 4.0.6 on 2022-07-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0009_rename_tags_booking_payment_remove_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
