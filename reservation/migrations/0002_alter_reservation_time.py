# Generated by Django 4.0.4 on 2022-07-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
