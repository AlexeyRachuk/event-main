from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from about.models import About


# Подключение CKEditor
class AboutAdminForm(forms.ModelForm):
    about_text_left = forms.CharField(label='Текст левого блока', widget=CKEditorUploadingWidget())
    about_text_right = forms.CharField(label='Текст правого блока', widget=CKEditorUploadingWidget())
    about_text_underline = forms.CharField(label='Текст блока под линией', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


# Блок О нас в админке
@admin.register(About)
class AboutAdminInline(SingletonModelAdmin):
    fields = ['about_title', 'about_text_left', 'about_button_one_title', 'about_button_one_url',
              'about_button_two_title', 'about_button_two_url', 'about_text_right', 'about_text_underline']
    form = AboutAdminForm
