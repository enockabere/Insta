from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Image, User
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='accounts/login/')
def home(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        post = Image.objects.create(
            description = data['description'],
            image = image,
        )
        return redirect('home')
    images=Image.objects.all()
    return render(request,'profile/account.html', {"images":images})
@login_required(login_url='accounts/login/')
def account(request):
    try:
        if request.method == 'POST':
            data = request.POST
            dp = request.FILES.get('dp')
            profile = Profile.objects.create(
                dp = dp,
                bio = data['bio']
            )
            return redirect('personal')
        profile = Profile.objects.all()
        current = request.user.id
        # posts = User.objects.include(current)        
        return render(request,'profile/personal.html',{"current":current})
    except:
        raise Http404("Could not access")
   
    