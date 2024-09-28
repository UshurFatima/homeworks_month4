from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='movie_list'),
    path('movies/<int:id>/', views.MovieDetail.as_view()),
    path('movies/<int:id>/edit/', views.MovieEdit.as_view()),
    path('movies/add/', views.AddMovie.as_view(), name='add_movie'),
    path('movies/<int:id>/drop/', views.MovieDrop.as_view()),
    path('review/', views.Review.as_view()),

    path('movies/thriller/', views.ThrillerFilter.as_view()),
    path('movies/comedy/', views.ComedyFilter.as_view()),
    path('movies/fantasy/', views.FantasyFilter.as_view()),
]