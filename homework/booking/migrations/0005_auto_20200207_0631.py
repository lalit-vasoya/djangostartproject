# Generated by Django 3.0.2 on 2020-02-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20200205_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='timeslot',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
