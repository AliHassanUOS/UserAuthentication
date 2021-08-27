from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from .models import Userprofile






class EditProfileForm(UserChangeForm):

    password = None

    class Meta:
         model = User
         fields = ('username','first_name','last_name','email','date_joined','last_login')
         labels = {  'email': 'Email'}
    


         widgets = {

              'username' : forms.TextInput(attrs={'class':'form-control' }),
              'first_name' : forms.TextInput(attrs={'class':'form-control' }),
              'last_name' : forms.TextInput(attrs={'class':'form-control' }),
              'email' : forms.EmailInput(attrs={'class': 'form-control'}),
              'date_joined': forms.DateInput(attrs={'class': 'form-control'}),
              'last_login': forms.DateInput(attrs={'class': 'form-control'}),
             }


class OurForm(UserCreationForm):
    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password again",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',)
        labels = {  'email': 'Email'}
    


        widgets = {

              'username' : forms.TextInput(attrs={'class':'form-control' }),
              'first_name' : forms.TextInput(attrs={'class':'form-control' }),
              'last_name' : forms.TextInput(attrs={'class':'form-control' }),
              'email' : forms.EmailInput(attrs={'class': 'form-control'}),
        }

class OurLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nickname', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password','class': 'form-control'}))
    
    class Meta:
        model = AuthenticationForm
        fields = ('__all__')



class password_from(PasswordChangeForm):

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'nickname','class': 'form-control'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password','class': 'form-control'}))
    
    class Meta:
        model = PasswordChangeForm
        fields = ('__all__')


        widgets = {

           'old_password' : forms.PasswordInput(attrs={'class':'form-control' }),

            
        }





