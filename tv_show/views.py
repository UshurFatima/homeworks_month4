from django.shortcuts import get_object_or_404
from django.views import generic
from . import models, forms


class MovieList(generic.ListView):
    template_name = 'movies/movie_list.html'
    context_object_name = 'movie_list'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.all(). order_by('-id')


class MovieDetail(generic.DetailView):
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie_id'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)


class MovieEdit(generic.UpdateView):
    template_name = 'movies/movie_edit.html'
    form_class = forms.MovieForm
    success_url = '/movies/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)


class AddMovie(generic.CreateView):
    template_name = 'movies/add_movie.html'
    form_class = forms.MovieForm
    success_url = '/movies/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddMovie, self).form_valid(form=form)


class MovieDrop(generic.DeleteView):
    template_name = 'movies/movie_drop.html'
    success_url = '/movies/'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(models.Movie, id=movie_id)


class Review(generic.CreateView):
    template_name = 'movies/review.html'
    context_object_name = 'review'
    form_class = forms.ReviewForm
    success_url = '/movies/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Review, self).form_valid(form=form)


class ThrillerFilter(generic.ListView):
    template_name = 'movies/thriller.html'
    context_object_name = 'thriller'

    def get_queryset(self):
        return models.Movie.objects.filter(genre='thriller').all().order_by('-id')


class ComedyFilter(generic.ListView):
    template_name = 'movies/comedy.html'
    context_object_name = 'comedy'

    def get_queryset(self):
        return models.Movie.objects.filter(genre='comedy').all().order_by('-id')


class FantasyFilter(generic.ListView):
    template_name = 'movies/fantasy.html'
    context_object_name = 'fantasy'

    def get_queryset(self):
        return models.Movie.objects.filter(genre='fantasy').all().order_by('-id')
