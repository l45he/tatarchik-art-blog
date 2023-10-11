from django.shortcuts import render
from django.template import loader


# Create your views here.

def index(request):
    context = {
        'title': 'Tatarchik-Art | Главная страница'
    }
    return render(request, 'navigator/main_page.html', context)

def contacts(request):
    context = {
        'title': 'Tatarchik-Art | Контакты'
    }
    return render(request, 'navigator/contacts.html', context)