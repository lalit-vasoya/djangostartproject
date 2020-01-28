from django.contrib import admin
from .forms import BookForm
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=[
        "__str__",
    ]
    readonly_feilds=['updated','timestamp','added_by','last_edited_by']

    form=BookForm

admin.site.register(Book)#,BookAdmin)        
