# Generated by Django 4.1.2 on 2022-10-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=50, verbose_name='Заголовок блока')),
                ('about_text_left', models.TextField(verbose_name='Текст левой колонки')),
                ('about_button_one_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название первой кнопки')),
                ('about_button_one_url', models.CharField(blank=True, help_text='Может быть задана ссылка на блок через #', max_length=80, null=True, verbose_name='Ссылка первой кнопки')),
                ('about_button_two_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Название второй кнопки')),
                ('about_button_two_url', models.CharField(blank=True, help_text='Может быть задана ссылка на блок через #', max_length=80, null=True, verbose_name='Ссылка второй кнопки')),
                ('about_text_right', models.TextField(verbose_name='Текст правой колонки')),
                ('about_text_underline', models.TextField(verbose_name='Текст под чертой')),
            ],
        ),
    ]
