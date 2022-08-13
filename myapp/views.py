from urllib.request import Request
from django.shortcuts import render,redirect
from .models import signup
from .forms import signupform
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            myfrm=signupform(request.POST)
            if myfrm.is_valid():
                myfrm.save()
                print("signup successfully...!")
                return redirect('menu')
            else:
                print(myfrm.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            user=signup.objects.filter(username=unm,password=pas)
            if user:
                print("login successfully...!")

                request.session['user']=unm

                return redirect('menu')
            else:
                print("login failed...!")
    return render(request,'index.html')

def menu(request):
    user=request.session.get('user')
    return render(request,'menu.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
