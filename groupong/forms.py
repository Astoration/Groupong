from django import forms

from .models import Post
# from .models import Profile
from .models import Comment
from django.conf import settings

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

#class UserForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ['username', 'email', 'password']

#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model = Profile
		
class SignupForm(forms.Form):
    id = forms.CharField(label="ID",min_length=6 ,max_length=12, required=True)
    password = forms.CharField(label="PASSWORD", min_length=4, max_length=12, widget=forms.PasswordInput, required=True)
    email = forms.CharField(label="EMAIL", required=True)
class LoginForm(forms.Form):
    id = forms.CharField(label="ID",min_length=6 ,max_length=12, required=True)
    password = forms.CharField(label="PASSWORD", min_length=4, max_length=12, widget=forms.PasswordInput, required=True)
