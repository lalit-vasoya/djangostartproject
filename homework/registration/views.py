from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import messages
# Create your views here.

class RegistrationView(View):
    def get(self,request):
        rform=RegistrationForm()
        return render(request,'registration/registration.html',{'form':rform})

    def post(self,request):
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
        return render(request,'registration/registration.html',{'form':rform})
        
    
class LoginView(View):
    def get(self,request):
        lform=LoginForm()
        return  render(request,'registration/login.html',{'form':lform})

    def post(self,request):
        form1=AuthenticationForm(data=request.POST)
        if form1.is_valid():
            contact=form1.cleaned_data.get('contact')
            password=form1.cleaned_data.get('password')
            user=authenticate(contact=contact,password=password)
            if user is not None: 
                login(request,user)
            else:
                messages.error(request,'User Not Found please Enter Valid data')
        return  render(request,'registration/login.html',{'form':form1})
        
class LogoutView(View):

    def get(self,request):
        logout(request)
        return redirect("login")