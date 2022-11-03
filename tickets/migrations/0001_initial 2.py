# Generated by Django 4.1.2 on 2022-10-30 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BenefitIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_title', models.CharField(max_length=50, verbose_name='Название иконки')),
                ('icon_class', models.CharField(max_length=50, verbose_name='Класс иконки')),
            ],
            options={
                'verbose_name': 'Иконки приемуществ',
                'verbose_name_plural': 'Иконки приемуществ',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_title', models.CharField(max_length=50, verbose_name='Название билета')),
                ('ticket_price', models.ImageField(upload_to='', verbose_name='Цена билета')),
                ('ticket_descr', models.TextField(verbose_name='Описание билета')),
                ('ticket_order', models.SmallIntegerField(default=0, verbose_name='Порядок')),
                ('ticket_draft', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.CreateModel(
            name='TicketsBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets_blog_title', models.CharField(max_length=60, verbose_name='Заголвок блока')),
            ],
            options={
                'verbose_name': 'Заголовок блока',
            },
        ),
        migrations.CreateModel(
            name='TicketBenefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_benefit_title', models.CharField(max_length=50, verbose_name='Название приемущества')),
                ('ticket_benefit_order', models.SmallIntegerField(default=0, verbose_name='Порядок')),
                ('ticket_benefit_draft', models.BooleanField(default=True, verbose_name='Публикация')),
                ('id_ticket_benefit', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='id_ticket_benefit', to='tickets.tickets')),
                ('ticket_benefit_icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefit_icon', to='tickets.benefiticon')),
            ],
            options={
                'verbose_name': 'Приемущество билета',
                'verbose_name_plural': 'Приемущество билета',
            },
        ),
    ]
