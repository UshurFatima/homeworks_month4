from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', views.BookDetailView.as_view()),

    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('book_list_delete/', views.BookListDeleteView.as_view(), name='book_list_delete'),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view()),
    path('book_list_edit/', views.BookListEditView.as_view(), name='book_list_edit'),
    path('book_list/<int:id>/edit/', views.UpdateBookView.as_view()),

    path('search/', views.SearchView.as_view(), name='search'),

    path('myinfo/', views.myinfo_view),
    path('friend/', views.friend_view),
    path('time/', views.time_view),
]