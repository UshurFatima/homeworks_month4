from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


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
        book_id = get_object_or_404(models.Book, id=id)
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
