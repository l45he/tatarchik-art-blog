from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='blog_main'),
]