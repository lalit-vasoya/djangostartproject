from django.db import models
from registration.models import User,CleanerModel,CityModel
# Create your models here.


class BookingModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    cleaner=models.ForeignKey(CleanerModel,null=True,on_delete=models.SET_NULL)
    date=models.DateField()
    city=models.ForeignKey(CityModel,null=True,on_delete=models.SET_NULL)
    timeslot=models.IntegerField(null=True)

    def __str__(self):
        #if self.user.is_cleaner:
        return self.cleaner.user.first_name
        #return self.user.first_name