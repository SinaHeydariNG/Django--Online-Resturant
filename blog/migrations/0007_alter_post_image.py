# Generated by Django 4.0.4 on 2022-07-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comments_options_comments_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/163529.jpg', upload_to='blog/'),
        ),
    ]