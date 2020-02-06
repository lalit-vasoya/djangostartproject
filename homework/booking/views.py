from django.shortcuts import render
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import View
from .models import BookingModel
from registration.models import CleanerModel
from .forms import BookingForm,SLOT_CHOICE

class BookingView(View):
    
    def get(self,request):
        form=BookingForm()
        return render(request,'booking/bookcleaner.html',{'form':form})
    
    def post(self,request):
        form=BookingForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data.get('city')
            timeslot=form.cleaned_data.get('timeslot')
            date=form.cleaned_data.get('date')    
            book=BookingModel.objects.filter(city__name=city,timeslot=timeslot,date=date)
            print(book)
            # cleaner=CleanerModel.objects.filter(city__name=city)
            cleaner=CleanerModel.objects.filter(city__name=city).only('user')
            
            print(cleaner.exclude())

            abc=CleanerModel.objects.filter(city__name=city)
            print(abc)
            # BookingModel.objects.filter(city__name=city,timeslot=timeslot,date=date,cleaner=~Q(abc))
            # abc=CleanerModel.objects.filter(~Q(BookingModel.objects.filter(city__name=city,timeslot=timeslot,date=date)))
            # print(cleaner.difference(book))
        return HttpResponse(form.errors)