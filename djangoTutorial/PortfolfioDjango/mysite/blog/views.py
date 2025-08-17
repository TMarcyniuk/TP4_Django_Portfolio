from django.views.generic.list import ListView
from .models import Post  #el "." en .models significa que dentro de la app/carpeta en la que se encunetra
from django.shortcuts import render 
from django.utils import timezone


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "Post"  

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #usar posts para referirse al queryset
    return render(request, 'blog/index.html', {'posts': posts}) #los dobles corchetes dentro de index.html se imprimen en pantalla, cuando hay uno solo es solo código de python
