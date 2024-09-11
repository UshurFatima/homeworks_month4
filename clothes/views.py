from django.shortcuts import render
from . import models


def clothes_filter_view(request):
    if request.method == 'GET':
        kids_cloth = models.Cloth.objects.filter(tags__name='для детей').order_by('-id')
        adults_cloth = models.Cloth.objects.filter(tags__name='для взрослых').order_by('-id')
        pensioners_cloth = models.Cloth.objects.filter(tags__name='для пенсионеров').order_by('-id')
        return render(
            request,
            template_name='clothes.html',
            context={
                'kids_cloth': kids_cloth,
                'adults_cloth': adults_cloth,
                'pensioners_cloth': pensioners_cloth
            }
        )
