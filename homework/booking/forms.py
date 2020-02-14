
from django import forms
from booking.models import BookingModel
from registration.models import CityModel
from django.utils import timezone

SLOT_CHOICE=(
    (0,'-------'),
    (1,'10 AM-11 AM'),
    (2,'11 AM-12 PM'),
    (3,'12 PM-01 PM'),
    (4,'01 PM-02 PM'),
    (5,'02 PM-03 PM'),
    (6,'03 PM-04 PM'),
    (7,'04 PM-05 PM'),
    (8,'05 PM-06 PM'),
    (9,'06 PM-07 PM'),
)

class BookingForm(forms.Form):
    city=forms.ModelChoiceField(label="Select City",queryset=CityModel.objects.all())
    timeslot=forms.IntegerField(label="Select Time",widget=forms.Select(choices=SLOT_CHOICE,attrs={'class': 'form-control'}))
    date=forms.DateField(widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input','type':'date','id':'id_date'
        }))
    city.widget.attrs['class']='form-control'
    date.widget.attrs['min']=timezone.now().date()