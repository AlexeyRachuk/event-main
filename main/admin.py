from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from main.models import Main, Menu, BottomBanner, MainPlace


# Подключение CKEditor
class BottomBannerForm(forms.ModelForm):
    bottom_banner_descr = forms.CharField(label='Описание на баннере', widget=CKEditorUploadingWidget())

    class Meta:
        model = BottomBanner
        fields = '__all__'


# Меню в админке
class MenuInline(admin.TabularInline):
    model = Menu
    extra = 1


# Админка основных параметров
@admin.register(Main)
class MainInline(SingletonModelAdmin):
    fields = ['main_title', 'main_description', 'main_name', 'main_copywrite', 'main_fb', 'main_instagram', 'main_wa',
              'main_yt']
    inlines = [MenuInline]


# Админика нижнего баннера
@admin.register(BottomBanner)
class BottomBannerAdmin(SingletonModelAdmin):
    fields = ['bottom_banner_title', 'bottom_banner_descr', 'bottom_banner_button', 'bottom_banner_button_url']
    form = BottomBannerForm


# Админика места проведения
@admin.register(MainPlace)
class MainPlaceAdmin(SingletonModelAdmin):
    fields = ['main_place_block_title', 'main_place_title', 'main_place_address', 'main_place_email',
              'main_place_phone', 'main_place_map']
