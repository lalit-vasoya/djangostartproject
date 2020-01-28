from django.shortcuts import render
from django.views.generic.base import TemplateView,TemplateResponseMixin,ContextMixin
from django.views.generic import View
from django.http import HttpResponse
# """Create your views here."""




class AboutusTemplateView(TemplateView):
    template_name="aboutus.html"
    extra_context={"titile":"This is about us page"}
    # def get_context_data(self,*args,**kargs):
    #     context=super(AboutusTemplateView,self).get_context_data(*args,**kargs)
    #    # context["title"]="About Us Page"
    #     return context

    # def get(self,request,*args,**kargs):
    #     return HttpResponse("asajsdbkl")



class ContactusView(TemplateResponseMixin,View,ContextMixin):
    
    def get(self,request,*args,**kargs):    
        context=self.get_context_data(**kargs)
        context["title"]="Some new"
        return self.render_to_response(context)
    #    return HttpResponse("<h1>Contact us Page</h1>")