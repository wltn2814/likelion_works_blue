from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['passwordCheck']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':"이미 존재하는 아이디입니다."})
            except:
                password=request.POST.get("password")
                realname=request.POST.get("realname") #나중에 추가하기
                user = User.objects.create_user(
                    request.POST["username"],password=password)
                auth.login(request,user)
                return redirect('/')
        else:
            return render(request, 'signup.html', {'error':"비밀번호가 일치하지 않습니다."})
    else:
        return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':"아이디 혹은 비밀번호가 일치하지 않습니다."})
    else:
        return render(request,"login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("/")
    else:
        return render(request, 'signup.html')