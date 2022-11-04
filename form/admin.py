from django.contrib import admin

from form.models import Form


# Админка формы
@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    fields = ['form_name', 'form_email', 'form_subject', 'form_text']