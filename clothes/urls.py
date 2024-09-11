from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.clothes_filter_view),
]