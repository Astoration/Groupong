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
from django.contrib.auth import login
from django.contrib.auth import logout
# Create your views here.
def index(request):
	print(request.user.username)
	return render(request, 'groupong/index.html', {User : request.user.username})
def loginPage(request):
	return render(request,'groupong/login.html',{})

def registerPage(request):
	return render(request,'groupong/register.html',{})
def detail(req):
	return render(req,'groupong/detail.html',{})
def writePage(req):
	return render(req,'groupong/write.html',{})
def post(req):
	pass
def register(req):
        if req.method == 'POST':
			form_data = SignupForm(req.POST)
			if True:
				username = req.POST.get('userId')
				password = req.POST.get('password')
				email = req.POST.get('email')
				User.objects.create_user(username=username,email=email,password=password,first_name=req.POST.get('firstName'),last_name=req.POST.get('lastName'))
        return HttpResponseRedirect("/")
def logins(req):
	user = authenticate(username=req.POST.get("userId"),password=req.POST.get('password'))
	print(user)
	if user is not None:
		login(req,user);
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")
	
def logouts(req):
	logout(req)
	return HttpResponseRedirect("/")