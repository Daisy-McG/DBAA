# Generated by Django 4.0.5 on 2022-06-16 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='going',
        ),
        migrations.RemoveField(
            model_name='event',
            name='not_going',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to='event_images/'),
        ),
    ]
