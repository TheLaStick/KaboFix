from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from KaboFixApp.models import KaboRequest
# Create your views here.



def main_page(request):
    if request.user.is_authenticated:
        return render(request, "main.html")
    else:
        return redirect('/login')

def KaboLogin_page(request):
    if request.method == 'GET':
        admin = request.POST.get('admin', '')
        if request.user.is_authenticated:
            if not admin:
                return redirect('/')
            else:
                return redirect('/mainadmin')

        return render(request, 'KaboLogin.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        admin = request.POST.get('admin', '')

        if username == '' or password == '':
            messages.error(request, 'Заполните все поля!')
            return redirect('/login')

        # проверяем правильность логина и пароля
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if not admin:
                return redirect('/')
            else:
                return redirect('mainadmin/')
        else:
            messages.error(request, 'Неправильный логин или пароль!')
            return redirect('/login')

def KaboRegister_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'KaboRegister.html')
    if request.method == 'POST':
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        admin = request.POST.get('admin', '')
        if username == '' or password == '' or email == '':
            return HttpResponse("Заполните все поля")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Логин з    анят")

        # создаем пользователя
        user = User.objects.create_user(username, email, password)
        user.save()

        # "входим" пользователя
        login(request, user)
        if not admin:
            return redirect('/')
        else:
            return redirect('/mainadmin')

def KaboLogout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/login')

def KaboWrite_Page(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'GET':
        return render(request, "KaboWrite.html")
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        KaboRecords = KaboRequest()
        KaboRecords.name = name
        KaboRecords.text = text

        KaboRecords.author = request.user
        KaboRecords.save()
        return render(request, "KaboWriteLate.html")

def KaboRead_Page(request):
    if request.user.is_authenticated:
        claims = KaboRequest.objects.all()

        #KaboRequest.likes.objects.add(request.user)

        return render(request, "KaboRead.html", { 'claims' : claims })
    else:
        return redirect('/login')

#Админка

def Kabo_MainAdmin_Page(request):
    if request.user.is_authenticated:
        return render(request, 'mainAdmin.html')
    else:
        return redirect('/login')

def Kabo_ReadAdmin_Page(request):
    if request.user.is_authenticated:
        return render(request, 'readAdmin.html')
    else:
        return redirect('/login')