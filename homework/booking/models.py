from django.db import models
from django.db.models.signals import post_save
from registration.models import User,CleanerModel,CityModel
# from .signals import post_save_bookingmodel__sending_email
# Create your models here.


class BookingModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    cleaner=models.ForeignKey(CleanerModel,null=True,on_delete=models.SET_NULL)
    date=models.DateField()
    city=models.ForeignKey(CityModel,null=True,on_delete=models.SET_NULL)
    timeslot=models.IntegerField(blank=False)

    def __str__(self):
        #if self.user.is_cleaner:
        return str(self.cleaner.user.first_name)
        #return self.user.first_name

# post_save.connect(post_save_bookingmodel__sending_email,sender=BookingModel)