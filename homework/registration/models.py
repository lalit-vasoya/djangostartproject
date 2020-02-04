from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class User(AbstractUser):
    contact = models.CharField('Contact',max_length=12,unique=True)
    first_name  = models.CharField('first_last',max_length=30,blank=True)
    last_name   = models.CharField('Last_last',max_length=30,blank=True)
    is_cleaner  = models.BooleanField('cleaner', default=False)

    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.contact