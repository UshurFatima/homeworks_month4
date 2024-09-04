from django.urls import path
from . import views

urlpatterns = [
    path('myinfo/', views.myinfo_view),
    path('friend/', views.friend_view),
    path('time/', views.time_view),
]