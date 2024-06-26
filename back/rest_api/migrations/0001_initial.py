# Generated by Django 5.0.3 on 2024-04-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('fam', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('otc', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('10+', '10+')], max_length=3, verbose_name='Количество путешественников')),
                ('continent', models.CharField(choices=[('AS', 'Азия'), ('AF', 'Африка'), ('EU', 'Европа'), ('LA', 'Латинская Америка'), ('AU', 'Австралазия ')], max_length=2, verbose_name='Континент')),
                ('type', models.CharField(choices=[('FAM', 'Семейный отдых'), ('HON', 'Медовый месяц'), ('CPL', 'Отдых для семейной пары'), ('SOL', 'Отдых для одного'), ('GRP', 'Отдых с группой друзей'), ('OTH', 'Другое')], max_length=3, verbose_name='Тип путешествия')),
            ],
        ),
    ]
