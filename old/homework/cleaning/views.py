from django.shortcuts import render,redirect
from django.views.generic import View
from .models import ProfileModel
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import messages
# Create your views here.

class RegistrationView(View):

    def get(self,request):
        rform=RegistrationForm()
        return render(request,'cleaning/registration.html',{'form':rform})

    def post(self,request):
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            obj=rform.save(commit=False)
            print(obj)
            rform.save()
            ProfileModel.objects.create(user=obj,phonenumber=rform.cleaned_data.get('phonenumber'),city=rform.cleaned_data.get('city'))
            #print(rform.cleaned_data)
        return render(request,'cleaning/registration.html',{'form':rform})
        
    
class LoginView(View):

    def get(self,request):
        lform=LoginForm()
        return  render(request,'cleaning/login.html',{'form':lform})

    def post(self,request):
        form1=LoginForm(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            password=form1.cleaned_data['password']
            mobile=form1.cleaned_data['phonenumber']
            user=authenticate(username=username,password=password)
            if user is not None: 
                if ProfileModel.objects.filter(phonenumber=mobile).exists():
                    login(request,user)
                    return redirect('registration')
                else:
                    messages.error(request,'Mobile Number Not Found')
            else:
                messages.error(request,'User Not Found please Enter Valid data')
        return  render(request,'cleaning/login.html',{'form':form1})
        
class LogoutView(View):
    def get(self,request):
        logout(request,request.user)
        return redirect("login")