# Generated by Django 4.0.3 on 2022-03-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default='8N6NR1', max_length=6),
        ),
    ]
