from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.

class BookDetailView(DetailView):
    model=Book

class BookListView(ListView):
    model=Book

    def get_queryset(self):
        return super().get_queryset()

    # def get_context_data(self,*args,**kargs):
    #     context=super().get_context_data(*args,**kargs)
    #     print(context)
    #     return context
