from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from streamblocks.models import ScheduleItem


# Подключение CKEditor
class ScheduleAdminForm(forms.ModelForm):
    decsr = forms.CharField(label='Описание события', widget=CKEditorUploadingWidget())

    class Meta:
        model = ScheduleItem
        fields = '__all__'


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    form = ScheduleAdminForm
