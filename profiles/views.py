from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Image, User
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='accounts/login/')
def home(request):
    images=Image.objects.all()
    return render(request,'profile/account.html', {"images":images})
@login_required(login_url='accounts/login/')
def account(request):
    try:
        current = request.user.id
        
        posts = Image.objects.exclude(user_id=current) 
        print(posts)
        return render(request,'profile/personal.html',{"posts":posts})
    except:
        raise Http404("Could not access")
   
    