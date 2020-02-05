from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegistrationForm,LoginForm,CleanerForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import messages
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import User
# Create your views here.

class ProfileDetailView(DetailView):
    model=User
    template_name="registration/profile.html"
    extra_context={'form':CleanerForm()}

class RegistrationView(View):
    def get(self,request):
        rform=RegistrationForm()
        return render(request,'registration/registration.html',{'form':rform})

    def post(self,request):
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
            messages.success(request,"Register Success Full Now Login !")
        return render(request,'registration/registration.html',{'form':rform})
        
    
class LoginView(View):
    def get(self,request):
        lform=LoginForm()
        return  render(request,'registration/login.html',{'form':lform})

    def post(self,request):
        form1=LoginForm(data=request.POST)
        if form1.is_valid():
            contact=form1.cleaned_data.get('contact')
            password=form1.cleaned_data.get('password')
            user=authenticate(contact=contact,password=password)
            if user is not None: 
                login(request,user)
                return redirect('registration:profile',pk=user.id)
            else:
                messages.error(request,'User Not Found please Enter Valid data'+str(form1.errors))
        return  render(request,'registration/login.html',{'form':form1})
        
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("registration:login")

""" Create A Cleaner """

class CleanerCreate(View):
    
    def post(self,request):
        form1=CleanerForm(request.POST)
        if form1.is_valid():
            obj=form1.save(commit=False)
            obj.user=request.user
            request.user.is_cleaner=True
            request.user.save()
            obj.save()
            return redirect("registration:profile",pk=request.user.pk)