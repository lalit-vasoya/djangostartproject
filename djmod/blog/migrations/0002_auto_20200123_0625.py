# Generated by Django 3.0.2 on 2020-01-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]