from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from datetime import datetime
from . import models, forms


class SearchView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_object'
    paginate_by = 5  # делит объекты по страницам

    def get_queryset(self):  # чтобы получать книги по q (то, что мы вводим в поиск)
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        # чтобы данные выводились по запросу (получаем их)
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')  # соединяем контекст с вьюшкой
        return context


class AddBookView(generic.CreateView):
    template_name = 'crud/add_book.html'
    form_class = forms.BookForm
    success_url = '/book_list/'

    def form_valid(self, form):
        print(form.cleaned_data)  # сохраняем информацию из формы
        # чтобы сохраненная информация отправилась в базу данных
        return super(AddBookView, self).form_valid(form=form)


# def add_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Книга была успешно добавлена! <a href = "/book_list/">На список книг</a>')
#     else:
#         form = forms.BookForm()
#     return render(
#         request,
#         template_name='crud/add_book.html',
#         context={
#             'form': form
#         }
#     )


class BookListDeleteView(generic.ListView):
    template_name = 'crud/book_list_delete.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class BookDropView(generic.DeleteView):
    template_name = 'crud/confirm_delete.html'
    success_url = '/book_list_delete/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


# def book_list_delete_view(request):
#     if request.method == "GET":
#         book_object = models.Book.objects.all()
#         return render(
#             request,
#             template_name='crud/book_list_delete.html',
#             context={
#                 'book_object': book_object
#             }
#         )


# def book_drop_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     return HttpResponse('Книга была успешно удалена! <a href = "/book_list/">На список книг</a>')


class BookListEditView(generic.ListView):
    template_name = 'crud/book_list_edit.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class UpdateBookView(generic.UpdateView):
    template_name = 'crud/update_book.html'
    form_class = forms.BookForm
    success_url = '/book_list_edit/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


# def book_list_edit_view(request):
#     if request.method == "GET":
#         book_object = models.Book.objects.all()
#         return render(
#             request,
#             template_name='crud/book_list_edit.html',
#             context={
#                 'book_object': book_object
#             }
#         )


# def update_book_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Информация о книге была успешно отредактирована! '
#                                 '<a href = "/book_list/">На список книг</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#
#     return render(
#         request,
#         template_name='crud/update_book.html',
#         context={
#             'form': form,
#             'book_id': book_id
#         }
#     )


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'book_object'
    model = models.Book

    def get_queryset(self):  # метод, отвечающий за вывод данных, только общий список
        return self.model.objects.all().order_by('-id')


# def book_list_view(request):
#     if request.method == "GET":
#         book_object = models.Book.objects.all()
#         return render(
#             request,
#             template_name='book_list.html',
#             context={
#                 'book_object': book_object
#             }
#         )


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')  # чтобы получить id из параметра kwargs
        return get_object_or_404(models.Book, id=book_id)


# def book_detail_view(request, id):
#     if request.method == "GET":
#         book_id = get_object_or_404(models. Book, id=id)
#         return render(
#             request,
#             template_name='book_detail.html',
#             context={
#                 'book_id': book_id
#             }
#         )


def myinfo_view(request):
    return HttpResponse('Привет!! Меня зовут Фатима, мне 16 лет и я учусь в школе.')


def friend_view(request):
    return HttpResponse('Нуржамал - моя подруга. Мы учились вместе с первого класса.')


def time_view(request):
    return HttpResponse(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
