# Generated by Django 3.2 on 2021-04-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='quiz_detail',
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
