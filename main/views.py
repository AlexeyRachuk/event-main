from django.shortcuts import render

from main.models import Main


# Представление основных параметров
def main(request):
    return render(request, 'index.html', {'all_main': Main.objects.all()})