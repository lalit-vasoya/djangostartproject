from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class CityModel(models.Model):
    ''' Model for city '''
    name=models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return self.name
    

class ProfileModel(models.Model):
    ''' Extend user model of django for customer as well as cleaner '''
    user        = models.OneToOneField(User,on_delete=models.PROTECT)
    phonenumber = models.CharField(max_length=12,unique=True,null=False,blank=False)
    city        = models.ForeignKey(CityModel,on_delete=models.PROTECT)
    ptype       = models.BooleanField(default=False,null=False,blank=True)

    def __str__(self):
        return self.user.username

