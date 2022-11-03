from django.db import models


# Заголовок блока
class TicketsBlock(models.Model):
    tickets_blog_title = models.CharField('Заголвок блока', max_length=60)

    def __str__(self):
        return "Заголовок блока"

    class Meta:
        verbose_name = "Заголовок блока"


# Карточки цен
class Tickets(models.Model):
    ticket_title = models.CharField('Название билета', max_length=50)
    ticket_price = models.IntegerField('Цена билета')
    ticket_descr = models.TextField('Описание билета')
    ticket_order = models.SmallIntegerField('Порядок', default=0)
    ticket_draft = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.ticket_title

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"


# Иконки приемуществ
class BenefitIcon(models.Model):
    icon_title = models.CharField('Название иконки', max_length=50)
    icon_class = models.CharField('Класс иконки', max_length=50)

    def __str__(self):
        return self.icon_title

    class Meta:
        verbose_name = "Иконки приемуществ"
        verbose_name_plural = "Иконки приемуществ"


# Примещуства билета
class TicketBenefit(models.Model):
    ticket_benefit_icon = models.ForeignKey(BenefitIcon, on_delete=models.CASCADE, verbose_name='ticket_benefit_icon',
                                            name='Иконка приемущества', null=True)
    ticket_benefit_title = models.CharField('Название приемущества', max_length=50)
    ticket_benefit_order = models.SmallIntegerField('Порядок', default=0)
    ticket_benefit_draft = models.BooleanField('Публикация', default=True)
    id_ticket_benefit = models.ForeignKey(Tickets, on_delete=models.CASCADE, related_name='id_ticket_benefit',
                                          default='')

    def __str__(self):
        return self.ticket_benefit_title

    class Meta:
        verbose_name = "Приемущество билета"
        verbose_name_plural = "Приемущество билета"
