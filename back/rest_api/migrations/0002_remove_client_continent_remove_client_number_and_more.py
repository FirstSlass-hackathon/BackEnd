# Generated by Django 5.0.3 on 2024-04-11 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='client',
            name='number',
        ),
        migrations.RemoveField(
            model_name='client',
            name='otc',
        ),
        migrations.RemoveField(
            model_name='client',
            name='type',
        ),
    ]
