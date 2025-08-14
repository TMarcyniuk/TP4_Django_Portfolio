from django.views.generic.list import ListView
from .models import Post  
from django.shortcuts import render


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "Post"  

def post_list(request):
    return render(request, 'blog/index.html', {})
