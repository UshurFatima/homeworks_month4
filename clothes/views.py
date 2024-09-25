from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page
from . import models


@method_decorator(cache_page(60*15), name='dispatch')
class ClothesFilterView(generic.ListView):
    template_name = 'clothes.html'
    context_object_name = 'kids_cloth' 'adults_cloth' 'pensioners_cloth'
    model = models.Cloth

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kids'] = models.Cloth.objects.filter(tags__name='для детей').order_by('-id')
        context['adults'] = models.Cloth.objects.filter(tags__name='для взрослых').order_by('-id')
        context['pensioners'] = models.Cloth.objects.filter(tags__name='для пенсионеров').order_by('-id')
        return context

# def clothes_filter_view(request):
#     if request.method == 'GET':
#         kids_cloth = models.Cloth.objects.filter(tags__name='для детей').order_by('-id')
#         adults_cloth = models.Cloth.objects.filter(tags__name='для взрослых').order_by('-id')
#         pensioners_cloth = models.Cloth.objects.filter(tags__name='для пенсионеров').order_by('-id')
#         return render(
#             request,
#             template_name='clothes.html',
#             context={
#                 'kids_cloth': kids_cloth,
#                 'adults_cloth': adults_cloth,
#                 'pensioners_cloth': pensioners_cloth
#             }
#         )
