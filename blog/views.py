from django.shortcuts import render  # для преобразования моделей, html-шаблонов, логики
from django.http import HttpResponse


def hello_view(request):
    return HttpResponse('hello world!!!')
