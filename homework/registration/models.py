from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class User(AbstractUser):
    username= models.CharField('username',max_length=12)
    contact = models.CharField('Contact',max_length=10,unique=True)
    first_name  = models.CharField('first_last',max_length=30)
    last_name   = models.CharField('Last_last',max_length=30)
    is_cleaner  = models.BooleanField('cleaner', default=False)

    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.contact)

    def get_absolute_url(self):
        return reverse("registration:profile", kwargs={"pk": self.pk})
    
class CityModel(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class CleanerModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    quality_score = models.FloatField(default=0)
    city=models.ForeignKey(CityModel,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.first_name

    def get_absolute_url(self):
        return reverse("booking:cleanerconfirm", kwargs={"pk": self.pk})
    
