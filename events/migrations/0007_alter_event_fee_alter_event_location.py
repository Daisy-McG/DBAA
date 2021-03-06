# Generated by Django 4.0.5 on 2022-06-18 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_fee_event_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fee',
            field=models.DecimalField(decimal_places=2, default=0, help_text='$', max_digits=5),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(default='Not Provided', max_length=160),
        ),
    ]
