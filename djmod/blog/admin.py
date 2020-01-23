from django.contrib import admin

from .models import PostModel
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):

    fields=[
        'title','slug','content','publish','publish_date','active','timestamp','updated',
        'get_age'
    ]
    readonly_fields=["timestamp","updated","get_age"]
    
    def get_age(self,obj,*args,**kwargs):
        return str(obj.age())

    class Meta:
        model=PostModel

admin.site.register(PostModel,PostModelAdmin )