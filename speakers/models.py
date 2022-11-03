from django.db import models


# Модель спикеров основные
class SpeakersMain(models.Model):
    title = models.CharField('Заголвок блока', max_length=50)
    descr = models.TextField('Описание блока')

    def __str__(self):
        return "Настройки блока Спикеров"

    class Meta:
        verbose_name = "Настройки блока Спикеров"


# Модель спикеров. Спикеры.
class Speakers(models.Model):
    speakers_title = models.CharField('ФИО спикера', max_length=100)
    speakers_descr = models.CharField('Долдность спикера', max_length=70)
    speakers_inst = models.CharField('Инстаграмм спикера', max_length=100, null=True, blank=True)
    speakers_photo = models.ImageField('Фото спикера', upload_to='photo/')
    speakers_main = models.BooleanField('Избранный спикер?', default=False)
    speakers_order = models.SmallIntegerField('Порядок', default=0)
    speakers_draft = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.speakers_title

    class Meta:
        verbose_name = "Спикеры"
        verbose_name_plural = "Спикеры"
