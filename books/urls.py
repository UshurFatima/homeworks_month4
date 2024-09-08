from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view),
    path('book_list/<int:id>/', views.book_detail_view),

    path('myinfo/', views.myinfo_view),
    path('friend/', views.friend_view),
    path('time/', views.time_view),
]