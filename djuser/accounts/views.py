from django.shortcuts import render
from django.views.generic import View
from .forms import RegistrationForm 
# Create your views here.

class RegistrationView(View):
    
    def get(self,request):
        rform=RegistrationForm()
        #a=super(RegistrationView,self).get(request,*args,**kwargs)
        #print('getmethod')
        return render(request,"accounts/registration.html",{'form':rform})

    def post(self,request):
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save(commit=False)

        return render(request,"accounts/registration.html",{'form':rform})