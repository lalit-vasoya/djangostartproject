# Generated by Django 3.0.2 on 2020-02-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='timeslot',
            field=models.SmallIntegerField(choices=[(1, '10-11'), (2, '11-12'), (3, '12-01'), (4, '01-02'), (5, '02-03'), (6, '03-04'), (7, '04-05'), (8, '05-06'), (9, '06-07')]),
        ),
    ]
