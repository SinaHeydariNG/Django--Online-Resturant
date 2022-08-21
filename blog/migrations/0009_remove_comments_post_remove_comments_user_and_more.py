# Generated by Django 4.0.4 on 2022-08-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comments_post_alter_comments_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='post_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
    ]