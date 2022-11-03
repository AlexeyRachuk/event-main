from django.db import models
from datetime import date

from streamfield.fields import StreamField
from streamblocks.models import ScheduleItem


# Заголовок блока Расписание
class TitleSchedule(models.Model):
    title = models.CharField('Заголовок блока', max_length=60)

    def __str__(self):
        return "Заголовок блока"

    class Meta:
        verbose_name = "Заголовок блока"


# Заголовок и дата проведения
class Schedule(models.Model):
    title_schedule = models.CharField('Название дня', max_length=50)
    date_schedule = models.DateField('Дата проведения', default=date.today)
    id_schedule = models.CharField('ID вкладки', max_length=50, help_text='Пример: day_1')

    def __str__(self):
        return self.title_schedule

    class Meta:
        verbose_name = "День проведения"
        verbose_name_plural = "День проведения"


class ScheduleOnPage(models.Model):
    stream = StreamField(
        model_list=[
            ScheduleItem,
        ],
        verbose_name="Расписание"
    )
    id_schedule_item = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='id_schedule_item',
                                         default='')

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
