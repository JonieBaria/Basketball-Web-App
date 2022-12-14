# Generated by Django 4.0.6 on 2022-07-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court', models.CharField(max_length=200, null=True)),
                ('schedule', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('statman', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='date_booked',
        ),
    ]
