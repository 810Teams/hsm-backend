# Generated by Django 2.2 on 2019-04-18 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_room_room_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingdetail',
            options={'verbose_name': 'Booking Detail', 'verbose_name_plural': 'Booking Details'},
        ),
    ]
