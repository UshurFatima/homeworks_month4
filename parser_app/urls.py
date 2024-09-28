from django.urls import path
from . import views

urlpatterns = [
    path('start_parsing/', views.ParserFormView.as_view()),
    path('rezka_movie_list/', views.RezkaMovieListView.as_view(), name='manas_film_list'),
]
