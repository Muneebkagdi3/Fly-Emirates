from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout






def User_register(request):

    if request.method == "GET":
        form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUSerCreationForm(request.POST)
        if form.is_valid():
          form.save()
    
    return render(request,"register.html", {"form":form})

def User_login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

    user = authenticate(username = username, password= password)

    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/")


def User_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")


