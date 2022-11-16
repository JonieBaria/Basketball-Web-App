# Generated by Django 4.0.6 on 2022-07-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametime', '0003_booking_player_booking_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='tags',
            field=models.ManyToManyField(to='gametime.tag'),
        ),
    ]