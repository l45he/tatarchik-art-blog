from django.shortcuts import render
from django.template import loader


# Create your views here.

def index(request):
    return render(request, 'navigator/main_page.html')

def contacts(request):
    return render(request, 'navigator/contacts.html')