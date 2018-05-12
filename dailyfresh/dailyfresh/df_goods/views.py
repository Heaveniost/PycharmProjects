#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1


def list(request):
    return render(request,'df_user/list.html')


def detail(request):
    return render(request,'df_user/detail.html')

