# Generated by Django 2.1.4 on 2018-12-22 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_remove_feedback_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='url',
        ),
    ]
