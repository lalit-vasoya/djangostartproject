from django.contrib import admin
from .models import User,CityModel,CleanerModel
# Register your models here.

admin.site.register(User)
admin.site.register(CityModel)
admin.site.register(CleanerModel)
