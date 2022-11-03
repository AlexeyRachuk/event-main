from django.db import models


# Модель основных параметров
class Main(models.Model):
    main_title = models.CharField('Title страницы', max_length=80)
    main_description = models.CharField('Description страницы', max_length=255)
    main_name = models.CharField('Название сайта', max_length=100)
    main_copywrite = models.CharField('Копирайт в подвале', max_length=150)
    main_fb = models.CharField('FB в подвале', max_length=100, null=True, blank=True)
    main_instagram = models.CharField('Instagram в подвале', max_length=100, null=True, blank=True)
    main_wa = models.CharField('WA в подвале', max_length=100, null=True, blank=True)
    main_yt = models.CharField('YouTube в подвале', max_length=100, null=True, blank=True)

    def __str__(self):
        return "Настройки"

    class Meta:
        verbose_name = "Настройки"


# Модель меню
class Menu(models.Model):
    menu_title = models.CharField('Пукнт меню', max_length=50)
    menu_url = models.CharField('Ссылка меню', max_length=50)
    menu_footer = models.BooleanField('Отображать пункт меню в подвале', default=False)
    menu_order = models.SmallIntegerField('Порядок', default=0)
    menu_draft = models.BooleanField('Публикация', default=True)
    id_menu = models.ForeignKey(Main, on_delete=models.CASCADE, related_name='id_menu', default='')

    class Meta:
        verbose_name = "Пункты меню"
        verbose_name_plural = "Пункты меню"


# Модель нижнего баннера
class BottomBanner(models.Model):
    bottom_banner_title = models.CharField('Заголовок баннера', max_length=50)
    bottom_banner_descr = models.TextField('Описание на баннере')
    bottom_banner_button = models.CharField('Название кнопки', max_length=50)
    bottom_banner_button_url = models.CharField('Ссылка на кнопку', max_length=80,
                                                help_text='Может быть задана ссылка на блок через #')

    def __str__(self):
        return "Нижний баннер"

    class Meta:
        verbose_name = "Нижний баннер"


# Модель места проведения
class MainPlace(models.Model):
    main_place_block_title = models.CharField('Заголовок блока', max_length=50)
    main_place_title = models.CharField('Название места', max_length=60)
    main_place_address = models.CharField('Адрес', max_length=100)
    main_place_email = models.EmailField('Email', max_length=100)
    main_place_phone = models.CharField('Телефон', max_length=20)
    main_place_map = models.CharField('Ссылка на карту', max_length=255, help_text='Скрипт или фрэйм карты')

    def __str__(self):
        return "Место проведения"

    class Meta:
        verbose_name = "Место проведения"
