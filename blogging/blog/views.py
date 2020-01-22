from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Post
from django.contrib.auth.decorators import login_required
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
    
    #if request.user.is_authenticated:
    #    return render(request,"blog/post_list.html",{"query":p})
    #else:
        #raise Http404
    #    return render(request,"blog/unauthentication.html")
    #print(path.join(BASE_DIR,'templates'))
    #print(p[0].text)
    #return HttpResponse("Hello World!")