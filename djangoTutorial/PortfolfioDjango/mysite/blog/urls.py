from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.post_list, name='posts_lists'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #el int:pk significa que django va a buscar el post que tenga el numero equivalente al int (ej: blog/post/3/)
]