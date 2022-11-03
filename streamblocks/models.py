from django.db import models
from django.utils.timezone import now

from speakers.models import Speakers


# Элементы расписания
class ScheduleItem(models.Model):
    title = models.CharField('Название собития', max_length=100)
    decsr = models.TextField('Описание события')
    photo = models.ImageField('Фото события', upload_to='photo/')
    speaker = models.ForeignKey(Speakers, on_delete=models.PROTECT, related_name='speaker_schedule', blank=True,
                                null=True)
    time_begin = models.TimeField('Время начала', default=now)
    time_end = models.TimeField('Время окончания', default=now)
    date_ivent = models.ManyToManyField(to='schedule.Schedule', verbose_name='Даты ивента',
                                            related_name='ivent_date')
    place = models.CharField('Место проведения', max_length=60)
    draft = models.BooleanField('Публикация', default=True)

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"


# Стим-блок
STREAMBLOCKS_MODELS = [
    ScheduleItem,
]
