from django.contrib import admin
from solo.admin import SingletonModelAdmin

from banner.models import BannerVideo, Banner


# Видео с баннера в админке
class VideoInline(admin.TabularInline):
    model = BannerVideo
    extra = 1


# Баннер в админке
@admin.register(Banner)
class BannerInline(SingletonModelAdmin):
    fields = ['banner_title_one', 'banner_title_two', 'banner_date', 'banner_plase', 'banner_movie']
    inlines = [VideoInline]
