from django.shortcuts import render,redirect,get_object_or_404,reverse
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.views.generic import View,DetailView,ListView
from .models import BookingModel
from registration.models import CityModel
from registration.models import CleanerModel
from .forms import BookingForm,SLOT_CHOICE
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core import serializers

@method_decorator(login_required, name='dispatch')
class SearchBookView(View):    
    def get(self,request):
        form=BookingForm()
        return render(request,'booking/searchcleaner.html',{'form':form})
    
    def post(self,request):
        form=BookingForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data.get('city')
            timeslot=form.cleaned_data.get('timeslot')
            date=form.cleaned_data.get('date')
            request.session['city']     = str(city)
            request.session['timeslot'] = str(timeslot)
            request.session['date']     = str(date)
            book=BookingModel.objects.filter(city__name=city,timeslot=timeslot,date=date)
            cleaner=CleanerModel.objects.filter(city__name=city).exclude(user__in=[x.cleaner.user for x in book]).exclude(user=request.user).order_by('-quality_score')
        return render(request,'booking/searchcleaner.html',{'cleaner':cleaner,'form':form,'date':date,"timeslot":timeslot,'range':range(5)})

class BookCleanerView(View):

    @method_decorator(login_required, name='dispatch')
    def get(self,request,pk):
        city=CityModel.objects.get(name=request.session['city'])
        book=BookingModel.objects.filter(city__name=city,timeslot=request.session['timeslot'] ,date=request.session['date'])
        cleaner=CleanerModel.objects.filter(city__name=city).exclude(user__in=[x.cleaner.user for x in book]).exclude(user=request.user)
        if cleaner:
            cleaner=CleanerModel.objects.get(id=pk)
            o=BookingModel.objects.create(user=request.user,city=city,date=request.session['date'],cleaner=cleaner,timeslot=request.session['timeslot'])
            ''' For Email Sending '''
            
                    
            return redirect('booking:booklist')
        else:
            return redirect('booking:searchbook')

@method_decorator(login_required, name='dispatch')
class BooklistListView(ListView):
    template_name='booking/booklist.html'
    
    def get_queryset(self):
        return BookingModel.objects.filter(user=self.request.user).order_by('-date','timeslot')

@method_decorator(login_required, name='dispatch')
class BookorderListView(ListView):
    template_name='booking/bookorder.html'

    def get_queryset(self):
        return BookingModel.objects.filter(cleaner__user=self.request.user).order_by('-date')

@method_decorator(login_required, name='dispatch')
class CleanerConfirm(View):
    def get(self,request,pk):
        cleaner=get_object_or_404(CleanerModel,pk=pk)
        return render(request,"booking/cleanerconfirm.html",{'cleaner':cleaner,'range':range(5)})