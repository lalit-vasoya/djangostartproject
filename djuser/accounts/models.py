from django.conf import settings

from django.contrib.auth.models import AbstractUser

from django.db import models
# from django.db.models.signals import post_save

# Create your models here.

# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.PROTECT)
#     city=models.CharField(max_length=120,blank=True,null=True)

#     def __str__(self):
#         return self.user.username


class User(AbstractUser):
    contact = models.CharField('Contact',max_length=12,unique=True)
    first_name  = models.CharField(max_length=30,blank=True)
    last_name   = models.CharField(max_length=30,blank=True)
    is_cleaner  = models.BooleanField('cleaner', default=True)

    USERNAME_FIELD = 'contact'
    REQUIRED_FIELD = ['username']

    def __str__(self):
        return self.contact