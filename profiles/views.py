from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'home.html')

# @login_required(login_url='accounts/login/')
def home(request):
    return render(request,'profile/account.html')