from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegistrationForm,LoginForm,CleanerForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import messages
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import User,CleanerModel

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model=User
    template_name="registration/profile.html"
    extra_context={'form':CleanerForm()}

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['form']=CleanerForm()
        if CleanerModel.objects.filter(user=self.request.user).exists():
            data['cleaner']=CleanerModel.objects.get(user=self.request.user)
            data['range']=range(5)
        return data

class RegistrationView(View):
    def get(self,request):
        rform=RegistrationForm()
        return render(request,'registration/registration.html',{'form':rform})

    def post(self,request):
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
            messages.success(request,"Register Success Full Now Login !")
            return redirect("registration:login")
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

@method_decorator(login_required, name='dispatch')
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
