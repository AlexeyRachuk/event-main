from django.contrib import admin
from django.utils.safestring import mark_safe
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from speakers.models import SpeakersMain, Speakers


# Подключение CKEditor
class SpeakersMainForm(forms.ModelForm):
    descr = forms.CharField(label='Описание блока', widget=CKEditorUploadingWidget())
    class Meta:
        model = SpeakersMain
        fields = '__all__'


# Основные параметры блока Спикеры в админке
@admin.register(SpeakersMain)
class SpeakersMainAdminInline(SingletonModelAdmin):
    fields = ['title', 'descr']
    form = SpeakersMainForm


# Спикеры в админке
@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ['speakers_title', 'speakers_descr', 'get_photo', 'speakers_main', 'speakers_order',
                    'speakers_draft']
    list_editable = ['speakers_main', 'speakers_order', 'speakers_draft']

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.speakers_photo.url} width="90" height="60"')

    get_photo.short_description = 'Фото спикера'
