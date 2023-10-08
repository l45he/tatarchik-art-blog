from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('contacts/', views.contacts, name='contacts'),
]