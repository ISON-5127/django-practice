#coding:utf-8
import transaction as transaction
from django.db import connection
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import User as user,Balance as balance
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .form import LoginForm
from django.views.decorators.csrf import csrf_exempt
# import psycopg2
import time

@csrf_exempt
def mylogin(request):
    error=[]
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            global p1
            p1=data['username']
            # counts=login_validate(request,username,password)
            if login_validate(request, username, password):
                # welcome.p1=username
                # sql = 'UPDATE user_balance SET balance=balance-1 WHERE username = %s'
                # cursor = connection.cursor()
                # cursor.execute(sql,[username])
                # p=balance.objects.raw('SELECT balance FROM user_balance WHERE username=username')
            # if counts:
                localt = time.asctime(time.localtime(time.time()))
                string = str(localt)
                # bal=p.balance
                return render_to_response('home.html', {'user': username,'string':string})
            else:
                error.append('Please input the correct password')
        else:
            error.append('Please input both username and password')
    else:
        form = LoginForm()
    return render_to_response('login.html', {'error': error, 'form': form})


def login_validate(request, username, password):
    rtvalue = False
    # sql='SELECT COUNT(*) FROM login_user WHERE username = %s and password = %s'
    # counts=user.objects.raw(sql,[username,password])
    # cursor = connection.cursor()
    # cursor.execute(sql,[username,password])
    cursor = connection.cursor()
    cursor.execute('SELECT count(*) from login_user WHERE username= %s and password=%s',[username,password])
    raw = cursor.fetchone()
    # return raw
    if raw[0] == 1L :
        return True
    return rtvalue



def welcome(request):
    localt = time.asctime(time.localtime(time.time()))
    string = str(localt)
    sql='UPDATE user_balance SET balance=balance-1 WHERE username = %s'
    cursor = connection.cursor()
    cursor.execute(sql,[p1])
    return render(request,'welcome.html',{'string':string})



def home(request):
    # p = user.objects.raw('SELECT * from user_balance')[0]
    # usern = p.user
    # p.balance=p.balance-1
    # bal = p.balance
    # p.save()
    # p=balance.objects.raw('SELECT * FROM user_balance')
    # usern=p.user
    # usern=mylogin.username

    # sql = 'UPDATE user_balance SET balance=balance-1 WHERE username=username'
    #
    # cursor = connection.cursor()
    # cursor.execute(sql)
    localt = time.asctime(time.localtime(time.time()))
    string=str(localt)
    return render(request, 'home.html',{'string':string})




# def mylogout(request):
#     auth_logout(request)
#     return HttpResponseRedirect('/login/')



# def login(request):
#     # username= request.GET['username']
#     # password= request.GET['password']
#     string='1'
#     return render(request, 'login.html',{'string':string})


def add(request):
    p=user(username=request.GET['username'],password=request.GET['password'])
    p.save()
    return HttpResponse('success.')


# def show(request):
#     # p=user.objects.raw('SELECT * from login_user')[1]
#     # result = p.username + str(p.password)
#
#     sql = 'SELECT * from login_user WHERE username="'+request.GET['username']+'"'
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result=cursor.fetchall()
#     return render(request,'show.html',{'result':result[0]})

def showCount(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute('SELECT count(*) from user_balance')
    raw = cursor.fetchone()
    return render(request, 'show.html',{'result': raw})

def recover(request):
    usern = request.GET['username']
    passw = request.GET['password']
    for i in (0,1):
        p = user.objects.raw('SELECT * from login_user')[i]
        if p.username == usern:
            p.password = passw
        elif p.password == passw:
            p.username = usern
        p.save()
    return HttpResponse('OK.')




def edit(request):
    usern = request.GET['username']
    passw = request.GET['password']
    # n = user.objects.raw('UPDATE login_user SET password=11111')
    # for i in (0,1):
    #     p = user.objects.raw('SELECT * from login_user')[i]
    #     if p.username == usern:
    #         p.password = passw
    #     elif p.password == passw:
    #         p.username = usern
    #     p.save()

    sql = 'UPDATE login_user SET password='+passw+' WHERE username='+usern

    cursor = connection.cursor()
    cursor.execute(sql)
    # transaction.commit_unless_managed()

    return HttpResponse('OK.')


def delete(request):
    usern = request.GET['username']
    # user.password= 111
    # request.GET['password']
    sql = 'DELETE FROM login_user WHERE username='+usern

    cursor = connection.cursor()
    cursor.execute(sql)

    return HttpResponse('SUCCESS.')



#
# def home(request):
#     localt=time.asctime(time.localtime(time.time()))
#     string=str(localt)
#     return render(request, 'home.html',{'string':string})