from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Menu, Basket, Pay
from .forms import SigninForm
from datetime import datetime
import random

#from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    signin_form = SigninForm()
    return render(request, 'main/home.html', {'signin_form': signin_form})

def signin(request):
    if request.method == "POST":
        u_id = request.POST['u_id']
        password = request.POST['password']
        user = authenticate(u_id = u_id, password = password)

        if user is not None:
            login(request, user)
            return redirect('mypage')
        else:
            messages.error(request,'회원정보가 일치하지 않습니다. 다시 시도해주세요.')
            return redirect('home')

def mypage(request):
    user = request.user
    por_list = Pay.objects.all()
    m_list = list()
    for m in Menu.objects.all():
        if m.user_id == user:
            m_list.append(m)

    return render(request, 'main/mypage.html', {'user':user, 'por_list':por_list, 'm_list':m_list})