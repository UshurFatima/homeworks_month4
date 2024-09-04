from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def myinfo_view(request):
    return HttpResponse('Привет!! Меня зовут Фатима, мне 16 лет и я учусь в школе.')


def friend_view(request):
    return HttpResponse('Нуржамал - моя подруга. Мы учились вместе с первого класса.')


def time_view(request):
    return HttpResponse(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
