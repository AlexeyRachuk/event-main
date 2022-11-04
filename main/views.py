from django.shortcuts import render

from form.forms import FormOnPage
from main.models import Main


# Представление основных параметров
def main(request):
    error = ''
    if request.method == 'POST':
        form = FormOnPage(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                error = 'Форма не была отправлена'
    else:
        form = FormOnPage()
    return render(request, 'index.html', {'form': form, 'error': error, 'all_main': Main.objects.all()})
