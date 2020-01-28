from django.shortcuts import render
from .models import Book
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 
from .forms import BookForm
from django.urls import reverse,reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

# Create your views here
class BookDetailView(DetailView):
    model=Book

class BookListView(ListView):
    model=Book

class BookCreateView(SuccessMessageMixin,CreateView):
    #model=Book
    form_class=BookForm
    template_name="cbview/form.html"
    #fields=["title","description"]  
    success_message="%(title)s is Created"

    def form_valid(self,form):
        print(form.instance)
        form.instance.added_by=self.request.user
        form.instance.last_edited_by=self.request.user 
        return super(BookCreateView,self).form_valid(form)

    def get_success_url(self):
        
        return reverse("book_list")

class BookUpdateView(UpdateView):
    model=Book
    form_class=BookForm 
    template_name="cbview/form.html"
    #fields=["title","description"]  
        
class BookDeleteView(SuccessMessageMixin,DeleteView):
    model=Book
    success_message="%(title)s is Delete"
    success_url=reverse_lazy("book_list")
    
    # def get_queryset(self):
    #     return super().get_queryset()

    # def get_context_data(self,*args,**kargs):
    #     context=super().get_context_data(*args,**kargs)
    #     print(context)
    #     return context
