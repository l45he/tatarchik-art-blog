from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

# Create your views here.
def blog_main(request):
    return render(request, 'blog/all_posts.html')

class PostsView(ListView):
    model = Posts #указываем модель с которой будем работать
    template_name = 'blog/all_posts.html' #указываем html-шаблон, который будет использоваться
    context_object_name = 'posts' #по какому названию сможем обращаться к данным, которые будут переданы внутрь шаблона
    ordering = ['-publication_date']