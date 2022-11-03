# Generated by Django 4.1.2 on 2022-10-30 06:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
import streamfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_schedule', models.CharField(max_length=50, verbose_name='Название дня')),
                ('date_schedule', models.DateField(default=datetime.date.today, verbose_name='Дата проведения')),
            ],
            options={
                'verbose_name': 'День проведения',
            },
        ),
        migrations.CreateModel(
            name='TitleSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Заголовок блока')),
            ],
            options={
                'verbose_name': 'Заголовок блока',
            },
        ),
        migrations.CreateModel(
            name='ScheduleOnPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', streamfield.fields.StreamField(blank=True, default='[]', verbose_name='Расписание')),
                ('id_schedule_item', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='id_schedule_item', to='schedule.schedule')),
            ],
        ),
    ]
