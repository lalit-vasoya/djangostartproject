
from django.db import models
from django.conf import settings
from django.urls import reverse
# from django.utils.encoding import smart_text
# from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
# from django.utils.timesince import timesince
# from .validation import validate_the_author_email

class Book(models.Model):
    added_by        = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name="book_add",on_delete=models.CASCADE)
    last_edited_by  = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name="book_edit",on_delete=models.CASCADE)
    title           = models.CharField(max_length=120,verbose_name="Title of Book")
    description     = models.TextField(null=True,blank=True,)
    slug            = models.SlugField()
    updated         = models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True,auto_now=False)

    class Meta:
        verbose_name="Book"
        ordering=["-id"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail",kwargs={"slug":self.slug})

def pre_save_book(sender,instance,*args,**kargs):
    slug=slugify(instance.title)
    instance.slug=slug

pre_save.connect(pre_save_book,sender=Book)
