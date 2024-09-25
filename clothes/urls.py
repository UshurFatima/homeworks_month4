from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.ClothesFilterView.as_view()),
]