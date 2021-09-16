from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile,Image, User
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from . forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    # if request.user:
    #     return redirect('home')
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
    all = User.objects.all()
    images=Image.objects.all()
    return render(request,'profile/account.html', {"images":images,"all":all})
@login_required(login_url='accounts/login/')
def account(request):

    if request.method == 'POST':
        data = request.POST
        dp = request.FILES.get('dp')
        print('data:',data)
        print('dp:',dp)
        
        profile = Profile.objects.create(
            dp = dp,
            bio = data['bio'],
            user = request.user
        )
        return redirect('personal')
    current = request.user.id
    posts = Image.objects.filter(user=current)
    all = Profile.objects.all()        
    return render(request,'profile/personal.html',{"posts":posts,"all":all})
   
def LikeView(request):
    post = get_object_or_404(Image, id=request.POST('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))
def updates(request):
    return HttpResponseRedirect(reverse('personal'))

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})