from django.shortcuts import render, get_object_or_404
from .models import Cosmonaut

def home(request):
    """Главная страница"""
    # Исключаем космонавтов, которые уже перечислены вручную на странице
    excluded_names = [
        'Герман Степанович Титов',
        'Сергей Константинович Крикалёв', 
        'Геннадий Иванович Падалка',
        'Анатолий Яковлевич Соловьёв',
        'Елена Владимировна Кондакова'
    ]
    
    # Получаем всех космонавтов из базы, исключая тех, кто уже есть вручную
    cosmonauts = Cosmonaut.objects.exclude(name__in=excluded_names).order_by('order')
    
    return render(request, 'pages/home.html', {
        'cosmonauts': cosmonauts,
    })

def titor(request):
    return render(request, 'pages/titor.html')

def soloviev(request):
    return render(request, 'pages/soloviev.html')

def padalka(request):
    return render(request, 'pages/padalka.html')

def krikalev(request):
    return render(request, 'pages/krikalev.html')

def kondakova(request):
    return render(request, 'pages/kondakova.html')

def cosmonaut_detail(request, pk):
    """Детальная страница космонавта из базы данных"""
    cosmonaut = get_object_or_404(Cosmonaut, pk=pk)
    return render(request, 'pages/cosmonaut_detail.html', {'cosmonaut': cosmonaut})