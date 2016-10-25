from django.shortcuts import render
from django.contrib.auth.models import User
# from .models import Profile
# from .forms import UserForm, UserProfileForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import forms
from .forms import SignupForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
	print(request.user)
	return render(request, 'groupong/index.html', {})

def loginPage(request):
	return render(request,'groupong/login.html',{})

def registerPage(request):
	return render(request,'groupong/register.html',{})
def detail(req):
	return render(req,'groupong/detail.html',{})
def register(req):
        if req.method == 'POST':
			form_data = SignupForm(req.POST)
			if True:
				username = req.POST.get('firstName')
				password = req.POST.get('password')
				email = req.POST.get('email')
				User.objects.create_user(username=username,email=email,password=password)
        return HttpResponseRedirect("/")
def login(req):
	user = authenticate(username=req.POST.get('email'), password=req.POST.get('password'))
	if user is not None:
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")