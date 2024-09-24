from django.shortcuts import render,redirect
from .forms import UserRegistration
from .models import User
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method =='POST':
        fm=UserRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            messages.success(request,'Data Saved Successfully')
        fm=UserRegistration()
    else:
        fm=UserRegistration()
    usr=User.objects.all()
    return render(request,'home.html',{'form':fm,'user':usr})

def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.success(request,'Data deleted successfully')
        return redirect('home')

def update(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        fm=UserRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        pi=User.objects.get(pk=id)
        fm=UserRegistration(instance=pi)
        return render(request,'update.html',{'form':fm})

