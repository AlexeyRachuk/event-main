from django.db import models


# Модель страницы О нас
class About(models.Model):
    about_title = models.CharField('Заголовок блока', max_length=50)
    about_text_left = models.TextField('Текст левой колонки')
    about_button_one_title = models.CharField('Название первой кнопки', max_length=50, null=True, blank=True)
    about_button_one_url = models.CharField('Ссылка первой кнопки', max_length=80, null=True, blank=True,
                                            help_text='Может быть задана ссылка на блок через #')
    about_button_two_title = models.CharField('Название второй кнопки', max_length=50, null=True, blank=True)
    about_button_two_url = models.CharField('Ссылка второй кнопки', max_length=80, null=True, blank=True,
                                            help_text='Может быть задана ссылка на блок через #')
    about_text_right = models.TextField('Текст правой колонки')
    about_text_underline = models.TextField('Текст под чертой')

    def __str__(self):
        return "Блок «О нас»"

    class Meta:
        verbose_name = "Блок «О нас»"
