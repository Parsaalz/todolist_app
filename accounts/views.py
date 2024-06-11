from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def signuppage(request):
    fr=SignupForm()
    if request.method=="POST":
        fr=SignupForm(data=request.POST)
        if fr.is_valid():
            username_t=fr.cleaned_data.get('username')
            password1_t=fr.cleaned_data.get('password1')
            password2_t=fr.cleaned_data.get('password2')
            new_user=User.objects.create_user(username=username_t,password=password1_t)
            new_user.save()
            return redirect('homepage')
    context={
        "fr":fr,
    }
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'signup.html',context)



def loginpage(request):
    fr=LoginForm()
    if request.method=="POST":
        fr=LoginForm(data=request.POST)
        if fr.is_valid():
            username_t=fr.cleaned_data.get('username')
            password_t=fr.cleaned_data.get('password')
            user_n=authenticate(request,username=username_t,password=password_t)
            if user_n:
                login(request,user_n)
                return redirect('dashboard')
    context={
        "fr":fr,
    }
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'login.html',context)


def logoutpage(request):
    logout(request)
    return redirect('homepage')