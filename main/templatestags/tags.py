from django import template

from about.models import About
from banner.models import Banner, BannerVideo
from main.models import Menu, BottomBanner, MainPlace
from schedule.models import TitleSchedule, Schedule
from speakers.models import SpeakersMain, Speakers
from streamblocks.models import ScheduleItem
from tickets.models import TicketsBlock, Tickets, TicketBenefit

register = template.Library()


# Меню в хедере
@register.inclusion_tag('tags/header_menu.html')
def get_header_menu():
    header_menu = Menu.objects.all().filter(menu_draft=True).order_by('menu_order')
    return {'header_menu_all': header_menu}


# Меню в футере
@register.inclusion_tag('tags/footer_menu.html')
def get_footer_menu():
    footer_menu = Menu.objects.all().filter(menu_draft=True, menu_footer=True).order_by('menu_order')
    return {'footer_menu_all': footer_menu}


# Баннер
@register.inclusion_tag('tags/banner.html')
def get_banner():
    banner = Banner.objects.all()
    return {'banner_all': banner}


# Видео в банере
@register.inclusion_tag('tags/banner_video.html')
def get_banner_video():
    banner_video = BannerVideo.objects.all().filter(video_draft=True).order_by('video_order')
    return {'banner_video_all': banner_video}


# Блок О нас
@register.inclusion_tag('tags/about_block.html')
def get_about_block():
    about_block = About.objects.all()
    return {'about_block_all': about_block}


# Блок спикеры
@register.inclusion_tag('tags/speakers.html')
def get_speakers():
    speakers_block = SpeakersMain.objects.all()
    return {'speakers_block_all': speakers_block}


# Список спикеров
@register.inclusion_tag('tags/speakers_items.html')
def get_speakers_items():
    speakers_item = Speakers.objects.all().filter().order_by()
    return {'speakers_item_all': speakers_item}


# Блок Расписание
@register.inclusion_tag('tags/schedule.html')
def get_schedule():
    schedule = TitleSchedule.objects.all()
    return {'schedule_all': schedule}


# Дни расписания
@register.inclusion_tag('tags/schedule_days.html')
def get_schedule_days():
    schedule_days = Schedule.objects.all().order_by('date_schedule')
    schedule_item = ScheduleItem.objects.all().order_by('time_begin').filter(draft=True)
    return {'schedule_days_all': schedule_days, 'schedule_item_all': schedule_item}


# Нижний баннер
@register.inclusion_tag('tags/bottom_banner.html')
def get_bottom_banner():
    bottom_banner = BottomBanner.objects.all()
    return {'bottom_banner_all': bottom_banner}


# Место проведения
@register.inclusion_tag('tags/place.html')
def get_place():
    place = MainPlace.objects.all()
    return {'place_all': place}


# Билеты
@register.inclusion_tag('tags/tickets.html')
def get_tickets():
    tickets_title = TicketsBlock.objects.all()
    tickets = Tickets.objects.all().filter(ticket_draft=True).order_by('ticket_order')
    tickets_benefit = TicketBenefit.objects.all().filter(ticket_benefit_draft=True).order_by('ticket_benefit_order')
    return {'tickets_title_all': tickets_title, 'tickets_all': tickets, 'tickets_benefit_all': tickets_benefit}
