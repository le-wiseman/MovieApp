from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index,name='home'),
    path('movies',views.movies,name='movies'),
    path('celebrities',views.celebrities,name='celebrities'),
    path('top-movies',views.topmovies,name='topmovies'),
    path('blog',views.blog,name='blog'),
    path('blog-details',views.blogdetails,name='blogdetails'),
    path('movie-details',views.moviedetails,name='moviedetails'),
]

urlpatterns += staticfiles_urlpatterns()