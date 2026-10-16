from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.book_edit, name="book_add"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("books/<int:pk>/delete/", views.book_delete, name="book_delete"),
    path("contacts/", views.contacts, name="contacts"),
    path("api/books/", views.api_books, name="api_books"),
    path("api/books/<int:pk>/", views.api_book_detail, name="api_book_detail"),
]
