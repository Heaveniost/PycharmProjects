from django.shortcuts import render
from django.http import HttpResponse


def login_views(request):
    return render(request,'login.html')


def register_views(request):
    return render(request,'register.html')
