# Generated by Django 4.1.2 on 2022-10-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_main_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='main_fb',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='FB в подвале'),
        ),
        migrations.AlterField(
            model_name='main',
            name='main_instagram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram в подвале'),
        ),
        migrations.AlterField(
            model_name='main',
            name='main_wa',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='WA в подвале'),
        ),
        migrations.AlterField(
            model_name='main',
            name='main_yt',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='YouTube в подвале'),
        ),
    ]
