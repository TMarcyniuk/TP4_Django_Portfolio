from django.views.generic.list import ListView
from .models import Project  

class IndexView(ListView):
    model = Project 
    template_name = "blog/index.html"
    context_object_name = "projects"  