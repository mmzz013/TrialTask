# Generated by Django 4.0.3 on 2022-03-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_user_username_alter_user_invite_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='invitation',
            new_name='invited_by',
        ),
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default='AM8944', max_length=6),
        ),
    ]
