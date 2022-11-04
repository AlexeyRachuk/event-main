from django.db import models

# Модель формы
class Form(models.Model):
    form_name = models.CharField('Имя', max_length=100)
    form_email = models.EmailField('Email', max_length=100)
    form_subject = models.CharField('Тема', max_length=100)
    form_text = models.TextField('Текст письма')

    class Meta:
        verbose_name = "Заявки с формы"
        verbose_name_plural = "Заявки с формы"

    def __str__(self):
        return "Заявки с формы"
