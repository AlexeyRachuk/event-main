from django.db import models


# Модель первого экрана
class Banner(models.Model):
    banner_title_one = models.CharField('Подчеркнутый текст', max_length=50)
    banner_title_two = models.CharField('Текст', max_length=50)
    banner_date = models.CharField('Даты проведения', max_length=50)
    banner_plase = models.CharField('Место проведения', max_length=50)
    banner_movie = models.FileField('Видео на фоне', upload_to='banner/')

    def __str__(self):
        return "Основной баннер"

    class Meta:
        verbose_name = "Основной баннер"


# Модель видео в баннере
class BannerVideo(models.Model):
    video_title = models.CharField('Название', max_length=50)
    video_url = models.CharField('Ссылка на видео', max_length=200)
    video_prew = models.ImageField('Превью видео', upload_to='banner/')
    video_order = models.SmallIntegerField('Порядок', default=0)
    video_draft = models.BooleanField('Публикация', default=True)
    id_video = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='id_video', default='')

    class Meta:
        verbose_name = "Видео в баннере"
        verbose_name_plural = "Видео в банере"
