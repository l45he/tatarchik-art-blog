from django.shortcuts import render
from django.views.generic import ListView
from .models import Artworks


# Create your views here.
def all_artworks(request):
    return render(request, 'portfolio/all_artworks.html')

class AllArtworksView(ListView):
    model = Artworks #указываем модель с которой будем работать
    template_name = 'portfolio/all_artworks.html' #указываем html-шаблон, который будет использоваться
    context_object_name = 'artworks' #по какому названию сможем обращаться к данным, которые будут переданы внутрь шаблона
    ordering = ['-id'] #указываем по какому полю производить сортировку (id, slug, title, desc, image -
    # поля нашей модели). Минус означает сортирову в обратном порядке

    # def get_context_data(self, *, object_list=None, **kwargs): #создаем объект контекста
    #     context = super(AllArtworks, self).get_context_data(**kwargs) #обращаемся через метод super() к родительскому классу
    #     artwork = Artworks.objects.filter(slug=self.kwargs['slug']).first()
    #
    #     context['title'] = Artworks.objects.filter(title=course).order_by('number')
    #     return context