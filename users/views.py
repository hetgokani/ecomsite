from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm 
# Create your views here.
from django.contrib.auth import logout
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render (request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')