from django.urls import path, include
from . import views 


app_name = "blog_post"
urlpatterns = [
    path('', views.post_list, name='posts_lists'),
]