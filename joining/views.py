#Import Libary
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
#Signup Function

def JoinUs(request):
    if request.method == "POST":
        return HttpResponse("Post Request")
    else:
        return render(request, "Home.html")


