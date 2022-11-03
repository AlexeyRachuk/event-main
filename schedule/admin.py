from django.contrib import admin
from solo.admin import SingletonModelAdmin

from schedule.models import TitleSchedule, Schedule, ScheduleOnPage


# Заголовок блока в админке
@admin.register(TitleSchedule)
class TitleScheduleAdmin(SingletonModelAdmin):
    fields = ['title', ]


# Элементы раписания в админке
class ScheduleOnPageAdmin(admin.TabularInline):
    model = ScheduleOnPage
    extra = 0


# Раписание в админке
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    fields = ['title_schedule', 'date_schedule', 'id_schedule']
    inlines = [ScheduleOnPageAdmin]
