# Generated by Django 4.0.4 on 2022-08-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=225)),
                ('copyright', models.CharField(max_length=225)),
            ],
        ),
    ]
