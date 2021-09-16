from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile,Image
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from . forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 

User = get_user_model()

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
    current = request.user.pk
    posts = Profile.objects.filter(user=current).all()
         
    return render(request,'profile/personal.html',{"posts":posts})
   
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

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})


# def search_user(request):
#     if 'search' in request.GET and request.GET["search"]:
#         search_term = request.GET.get('search')
#         searched_images = MyUserModel.search_by_username(search_term)
#         message = f"{search_term}"
#         return render (request,'search.html',{"message":message,"results":searched_images})
#     else:
#         message = "You have not searched for any term"
#         return render (request,'search.html',{"message":message})