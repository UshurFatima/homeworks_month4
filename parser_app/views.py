from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import models, forms


class ParserFormView(FormView):
    template_name = 'parser/parser_form.html'
    form_class = forms.Rezka

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные извлечены')
        else:
            return super(ParserFormView).post(request, *args, **kwargs)


class RezkaMovieListView(ListView):
    template_name = 'parser/movie_list.html'
    context_object_name = 'movie_list'
    model = models.ParserRezka

    def get_queryset(self):
        return self.model.objects.all()
