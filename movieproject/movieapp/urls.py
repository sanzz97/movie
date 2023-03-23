from django.urls import path
from . import views

app_name = 'movieapp' #for name space

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name = 'detail'), #to get detail page based on movie id, since movie-id is int -- int
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name = 'update'),
    path('delete/<int:id>/',views.delete,name = 'delete'),
]