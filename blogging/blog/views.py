from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Post
from django.contrib import messages
from .forms import Postform
# Create your views here.

#@login_required(login_url="account/login")

def home(request):
    p=Post.objects.all()
    return render(request,"blog/post_list.html",{"query":p})

def detail_view(request,id):
    p=get_object_or_404(Post,id=id)
    template="blog/detail_view.html"
    context={
        "i":p,
    }
    return render(request,template,context)

def create_view(request):
   
    form_a=Postform(request.POST or None)
    context={
        "form":form_a
    }
    if form_a.is_valid():
        obj=form_a.save(commit=False)
        obj.author=request.user
        obj.save()
        messages.success(request,f"Post {obj.title} Created")
        context={
            "form":Postform()
        }
        #return HttpResponseRedirect(f"/blog/{obj.id}")
      
    return render(request,"blog/create_view.html",context)    

def update_view(request,id=None):
    
    p=get_object_or_404(Post,id=id)
    form=Postform(request.POST or None,instance=p)
    context={
        "form":form
    }
    print("Hello")
    if form.is_valid():
        print(form.cleaned_data)
        print("Hello 2222")
        obj=form.save(commit=False)
        obj.author=request.user
        obj.save()
        return HttpResponseRedirect("/blog/")

    return render(request,"blog/update_view.html",context)

def delete_view(request,id=None):
    p=get_object_or_404(Post,id=id)
    if request.method=="POST":
        p.delete()
        messages.success(request,f"{p.title} Delete Suceess full")
        return HttpResponseRedirect("/blog/")
    return render(request,"blog/delete_view.html",{"post":p})
