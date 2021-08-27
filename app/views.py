from django.contrib.auth import forms
from django.contrib.messages.api import success
from django.contrib.messages.constants import SUCCESS
from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import OurForm, OurLoginForm,EditProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.



#Login Form function

def loginform(request):
    if not request.user.is_authenticated:


        if request.method == "POST":
            fmlogin = OurLoginForm(request=request, data = request.POST)
            if fmlogin.is_valid():
                uname = fmlogin.cleaned_data['username']
                upass = fmlogin.cleaned_data['password']
                obj=authenticate(username = uname , password = upass)
                if obj is not None:
                    login(request, obj)
                    messages.success(request,"Logedin Successfully ")
                    return HttpResponseRedirect('/profile/')
                    
        else:
            fmlogin = OurLoginForm()
                
        return render(request,'app/loginform.html', {'fmlogin': fmlogin})
    else:
        return HttpResponseRedirect('/profile/')




#Sing up Form Funcion
def formshow(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            fm = OurForm(request.POST)
            if fm.is_valid():
                fm.save()

            messages.add_message(request,SUCCESS,"User account has been created ")
        else:
            fm = OurForm()


        return render(request, "app/home.html", {"fm": fm})

    return HttpResponseRedirect('/profile/')



def profileform(request):

    if request.method == "POST":

        userform = EditProfileForm( request.POST ,instance=request.user) 

        if userform.is_valid():
            userform.save()
            messages.success(request,"Update Success")
        
    else:
        userform = EditProfileForm(instance=request.user) 


    return render(request,'app/profileform.html', {"userform":userform})
    
    


# logout

def user_logout(request):
    messages.warning(request,"Logout SuccessFully")

    logout(request)

    return HttpResponseRedirect("/login/")


# User Password Change

def password_change(request):

    if request.method == "POST":
        fm = PasswordChangeForm(request.user, data = request.POST)

        if fm.is_valid():

            fm.save()

            return HttpResponseRedirect("/profile/")
    else:
        fm = PasswordChangeForm(request.user)





   

    return render(request, "app/password_change.html", {'fm':fm})