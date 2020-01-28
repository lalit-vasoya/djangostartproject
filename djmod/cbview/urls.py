
from django.urls import path
from django.conf.urls import url
from .views import BookDetailView,BookListView,BookCreateView,BookUpdateView,BookDeleteView
from django.views.generic.list import ListView
from .models import Book
urlpatterns = [
    path('book/',ListView.as_view(model=Book),name="book_list"),
    path('book/create/',BookCreateView.as_view(),name="book_create"),
    path('book/<slug:slug>',BookDetailView.as_view(),name="book_detail"),
    path('book/<slug:slug>/update',BookUpdateView.as_view(),name="book_update"),
    path('book/<slug:slug>/delete',BookDeleteView.as_view(),name="book_delete")
]
