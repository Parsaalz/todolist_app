from django.shortcuts import render,redirect

def homepage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request,'home.html')
