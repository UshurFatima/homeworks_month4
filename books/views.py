from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models, forms


def add_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга была успешно добавлена! <a href = "/book_list/">На список книг</a>')
    else:
        form = forms.BookForm()
    return render(
        request,
        template_name='crud/add_book.html',
        context={
            'form': form
        }
    )


def book_list_delete_view(request):
    if request.method == "GET":
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='crud/book_list_delete.html',
            context={
                'book_object': book_object
            }
        )


def book_drop_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    book_id.delete()
    return HttpResponse('Книга была успешно удалена! <a href = "/book_list/">На список книг</a>')


def book_list_edit_view(request):
    if request.method == "GET":
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='crud/book_list_edit.html',
            context={
                'book_object': book_object
            }
        )


def update_book_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Информация о книге была успешно отредактирована! '
                                '<a href = "/book_list/">На список книг</a>')
    else:
        form = forms.BookForm(instance=book_id)

    return render(
        request,
        template_name='crud/update_book.html',
        context={
            'form': form,
            'book_id': book_id
        }
    )


def book_list_view(request):
    if request.method == "GET":
        book_object = models.Book.objects.all()
        return render(
            request,
            template_name='book_list.html',
            context={
                'book_object': book_object
            }
        )


def book_detail_view(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models. Book, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id
            }
        )


def myinfo_view(request):
    return HttpResponse('Привет!! Меня зовут Фатима, мне 16 лет и я учусь в школе.')


def friend_view(request):
    return HttpResponse('Нуржамал - моя подруга. Мы учились вместе с первого класса.')


def time_view(request):
    return HttpResponse(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
