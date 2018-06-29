#coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1


def register(request):
    return render(request,'df_user/register.html')


def register_handle(request):
    #接受用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码是否相同
    if upwd!=upwd2:
        return redirect('/user/register/')

    #密码加密
    # s1 = sha1()
    # s1.update(upwd)
    # upwd3 = s1.hexdiges


    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.email = uemail
    user.save()


    #注册成功 转到登录页
    return redirect('/user/login/')


# def register_exist(request):
#     uname = request.GET.get('uname')
#     count =UserInfo


def login(request):
    return render(request,'df_user/login.html')

#def login_handle(request):


# def info(request):
#     user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
#     context = {
#         'title':'用户中心',
#         'user_email': user_email,
#         'user_name': request.session['user_name']
#     }
#     return render(request,'df_user/user_center_info.html')


def index(request):
    return render(request, 'df_user/index.html')


def cart(request):
    return render(request, 'df_user/cart.html')


def place_order(request):
    return render(request, 'df_user/place_order.html')


def user_info(request):
    return render(request,'df_user/user_center_info.html')


def user_order(request):
    return render(request,'df_user/user_center_order.html')


def user_site(request):
    return render(request,'df_user/user_center_site.html')


def list(request):
    return render(request, 'df_user/list.html')


def detail(request):
    return render(request, 'df_user/detail.html')