from django.views.generic.list import ListView
from .models import Post  #el "." en .models significa que dentro de la app/carpeta en la que se encunetra
from django.shortcuts import render 
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "Post"  

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #usar posts para referirse al queryset
    return render(request, 'blog/index.html', {'posts': posts}) #los dobles corchetes dentro de index.html se imprimen en pantalla, cuando hay uno solo es solo código de python

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST": #despues de guardar el post manda la data como POST en vez de GET abajo en la terminal (no tiene que ver que un post del blog, solo es una coincidencia), esto es para cargarlo, aunque por ahora no tiene autor
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})