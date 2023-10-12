from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Artworks, Images


# Create your views here.
def all_artworks(request):
    return render(request, 'portfolio/all_artworks.html')

class AllArtworksView(ListView):
    model = Artworks #указываем модель с которой будем работать
    template_name = 'portfolio/all_artworks.html' #указываем html-шаблон, который будет использоваться
    context_object_name = 'artworks' #по какому названию сможем обращаться к данным, которые будут переданы внутрь шаблона
    ordering = ['-id'] #указываем по какому полю производить сортировку (id, slug, title, desc, image -
    # поля нашей модели). Минус означает сортирову в обратном порядке

    def get_context_data(self, *, object_list=None, **kwargs): #создаем объект контекста
        context = super(AllArtworksView, self).get_context_data(**kwargs) #обращаемся через метод super() к родительскому классу
        context['title'] = 'Tatarchik-Art | Мои работы'
        return context


class ArtworkView(DetailView):
    model = Artworks
    template_name = 'portfolio/one_artwork.html'
    ordering = ['-id']

    def get_context_data(self, object_list=None, **kwargs):
        artwork_name = Artworks.objects.filter(slug=self.kwargs['slug']).first()
        artwork_set = Images.objects.filter(artwork__slug=self.kwargs['slug'])
        context = super(ArtworkView, self).get_context_data(**kwargs)
        context['title'] = f'Tatarchik-Art | {artwork_name}'
        context['artwork_set'] = artwork_set
        return context