# Generated by Django 4.0.4 on 2022-07-27 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_comments_name_comments_post_comments_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
