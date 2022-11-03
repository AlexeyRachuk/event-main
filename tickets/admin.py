from django.contrib import admin
from solo.admin import SingletonModelAdmin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from tickets.models import TicketsBlock, BenefitIcon, TicketBenefit, Tickets


# Подключение CKEditor
class TicketsAdminForm(forms.ModelForm):
    ticket_descr = forms.CharField(label='Описание билета', widget=CKEditorUploadingWidget())

    class Meta:
        model = Tickets
        fields = '__all__'


# Заголовок блока в админке
@admin.register(TicketsBlock)
class TicketsBlocgAdmin(SingletonModelAdmin):
    fields = ['tickets_blog_title', ]


# Иконки в админке
admin.site.register(BenefitIcon)


# Приемущества билетов в админке
class TicketsBenefitInline(admin.TabularInline):
    model = TicketBenefit
    extra = 1


# Билеты в админке
@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['ticket_title', 'ticket_price', 'ticket_order', 'ticket_draft']
    list_editable = ['ticket_order', 'ticket_draft']
    inlines = [TicketsBenefitInline]
    form = TicketsAdminForm
