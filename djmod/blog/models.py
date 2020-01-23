from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save,post_save
from django.utils.timesince import timesince
from .validation import validate_the_author_email
PUBLISH_CHOICES=(
    ('draft','Draft'),
    ('publish','Publish'),
    ('private','Private'),
)

#use the model manager here to inherit this

class PostModelManager(models.Manager):
    # method is all method when PostModel.Objects.all()
    def all(self,*args,**kargs): 
        qs=super(PostModelManager,self).all(*args,**kargs).filter(active=True)
        print(qs)
        return qs

# Create your models here.
class PostModel(models.Model):
    id           = models.BigAutoField(primary_key=True)
    active       = models.BooleanField(default=True)
    title        = models.CharField(max_length=240,verbose_name="Post Title",unique=True,
                    error_messages={
                        "unique":"Please enter unique title"
                    },help_text="Title must be unique") 
    slug         = models.SlugField(null=True,blank=True)
    content      = models.TextField(null=True,blank=True)
    publish      = models.CharField(max_length=120,default="draft",choices=PUBLISH_CHOICES)
    view_count   = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
    author_email = models.EmailField(max_length=240,null=True,blank=True,validators=[validate_the_author_email])
    updated      = models.DateTimeField(auto_now=True)
    timestamp    = models.DateTimeField(auto_now_add=False,default=timezone.now)

    objects=PostModelManager() # creating a object of model.manager
    other=PostModelManager() # also call as PostModel.other.all()

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"
    
    def save(self,*args,**kargs):
        # if not self.slug and self.title:
        #     self.slug=slugify(self.title)
        super(PostModel,self).save(*args,**kargs)

    def __str__(self):
        return smart_text(self.title)

    def age(self):
        return timesince(self.publish_date)

def blog_post_model_pre_save(sender,instance,*args,**kwargs):
    print("before Save")
    

def blog_post_model_post_save(sender,instance,*args,**kargs):
    print("after save")
    if not instance.slug and instance.title:
        instance.slug=slugify(instance.title)
        instance.save()
    
pre_save.connect(blog_post_model_pre_save,sender=PostModel)
post_save.connect(blog_post_model_post_save,sender=PostModel)
