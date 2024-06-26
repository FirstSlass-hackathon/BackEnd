# Generated by Django 5.0.3 on 2024-04-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_remove_client_continent_remove_client_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='fam',
            field=models.CharField(max_length=10, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.TextField(max_length=15, null=True, verbose_name='Телефон'),
        ),
    ]
