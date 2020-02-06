
from django import forms
from .models import BookingModel
from registration.models import CityModel

SLOT_CHOICE=(
    (1,'10-11'),
    (2,'11-12'),
    (3,'12-01'),
    (4,'01-02'),
    (5,'02-03'),
    (6,'03-04'),
    (7,'04-05'),
    (8,'05-06'),
    (9,'06-07'),
)

class BookingForm(forms.Form):
    city=forms.ModelChoiceField(label="Select City",queryset=CityModel.objects.all())
    timeslot=forms.IntegerField(widget=forms.Select(choices=SLOT_CHOICE))
    date=forms.DateField(widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input','type':'date'
        }))