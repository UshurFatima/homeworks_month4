from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list_view),
    path('book_list/<int:id>/', views.book_detail_view),

    path('add_book/', views.add_book_view, name='add_book'),
    path('book_list_delete/', views.book_list_delete_view, name='book_list_delete'),
    path('book_list/<int:id>/delete/', views.book_drop_view),
    path('book_list_edit/', views.book_list_edit_view, name='book_list_edit'),
    path('book_list/<int:id>/edit/', views.update_book_view),

    path('myinfo/', views.myinfo_view),
    path('friend/', views.friend_view),
    path('time/', views.time_view),
]