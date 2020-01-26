
from django.urls import path
from django.conf.urls import url
from .views import BookDetailView,BookListView
from django.views.generic.list import ListView
from .models import Book
urlpatterns = [
    path('book/<slug:slug>',BookDetailView.as_view(),name="book_detail"),
    path('book/',ListView.as_view(model=Book),name="book_list")
]
