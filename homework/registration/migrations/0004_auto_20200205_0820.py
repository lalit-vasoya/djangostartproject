# Generated by Django 3.0.2 on 2020-02-05 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_citymodel_cleanermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanermodel',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.CityModel'),
        ),
    ]
