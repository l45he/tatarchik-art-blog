from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllArtworksView.as_view(), name='all_artworks'),
]