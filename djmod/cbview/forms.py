from .models import Book
from django import forms


class BookForm(forms.ModelForm):

    class Meta:
        model=Book
        fields=[
            'title','description',
        ]
    
    # def clean_title(self):
    #     print("Title is",self.cleaned_data["title"])
    #     raise forms.ValidationError("Title all ready exist")
    #     return self.cleaned_data["title"]