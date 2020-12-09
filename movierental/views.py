import json
from rest_framework import viewsets
from .models import Movie, Account, Actor, Cast, Customer, Moviequeue, Orders

from django.shortcuts import render, redirect
from django.views import View

import time

from django.contrib.sessions.models import Session
Session.objects.all().delete()

# Create your views here.
def homepage(request):
    qs = Movie.objects.all()

    cast_info = []
    for item in qs:
        casts = Cast.objects.filter(movieid=item.id)
        cast_info.append(casts)

    return render(request, 'homepage.html', {'qs' : qs, 'cast_info' : cast_info})

def login(request):
    response_data = {}

    if request.method == 'GET':
        return render(request, 'signin.html',{}) 

    elif request.method == 'POST':
        data = request.POST

        if not (data['email'] and data['name']):
            response_data['error'] = 'email과 이름을 모두 입력해주세요.'

        else:
            user = Customer.objects.get(email = data['email'])
            if user.name == data['name'] :
                request.session['user'] = user.id
                request.session['check'] = 1
                return redirect('/')

            else:
                response_data['error'] = '이름이 틀렸습니다.'

        return render(request, "signin.html", response_data)

def logout(request):
    request.session['check'] = 0
    request.session.pop('user')
    return redirect('/')

def user_page(request):
    user_id = request.session.get('user')
    user_info = Customer.objects.get(pk=user_id)  #pk : primary key
    account_info = Account.objects.get(customerid=user_id)
    return render(request, "user_page.html", {'user_info' : user_info, 'account_info' : account_info})

def edit_user_info(request):
    if request.method =='GET':
        return render(request, 'edituser.html')
    
    if request.method == 'POST':
        user_id = request.session.get('user')
        user_info = Customer.objects.get(pk=user_id)
        account_info = Account.objects.get(customerid=user_id)
        get_user_edit = request.POST.getlist('edit_info')
        get_account_edit = request.POST.getlist('edit_account')

        if len(get_user_edit[0])!=0:
            user_info.si = get_user_edit[0]
        if len(get_user_edit[1])!=0:
            user_info.gu = get_user_edit[1]
        if len(get_user_edit[2])!=0:
            user_info.creditcard = get_user_edit[2]
        if len(get_user_edit[3])!=0:
            user_info.email = get_user_edit[3]
        if len(get_user_edit[4])!=0:
            user_info.phonenumber = get_user_edit[4]
        user_info.save()
        if len(get_account_edit[0])!=0:
            account_info.accounttype = get_account_edit[0]
        if len(get_account_edit[1])!=0:
            account_info.acccreatetime = get_account_edit[1]
        account_info.save()

        return redirect('user_page')

def add_moviequeue(request):
    tmp = request.POST.getlist('sel_movie')
    if(len(tmp)>2):
        print('a')
    else:
        user_id = request.session.get('user')
        user_info = Customer.objects.get(pk=user_id)
        movie_info = Movie.objects.get(pk=tmp[0])
        moviequeue_info = Moviequeue.objects.filter(customerid=user_info)
        qn = len(moviequeue_info) + 1
        Moviequeue.objects.create(customerid=user_info, movieid=movie_info, queuenumber=qn)
    return redirect('/')

def get_moviequeue(request):
    qs = Moviequeue.objects.filter(customerid=request.session['user'])
    cast_info = []
    for item in qs:
        casts = Cast.objects.filter(movieid=item.movieid.id)
        cast_info.append(casts)
    print(cast_info)
    return render(request, "moviequeue.html", {'qs' : qs, 'cast_info' : cast_info})

def get_bestseller(request):
    qs = Movie.objects.all().order_by('-numcopies')

    cast_info = []
    for item in qs:
        casts = Cast.objects.filter(movieid=item.id)
        cast_info.append(casts)

    return render(request, "bestseller.html", {'qs' : qs, 'cast_info' : cast_info})

def search(request):
    search_movie = Movie.objects.all()
    q = request.POST.get('q',"")

    if q:
        movies = search_movie.filter(moviename__icontains=q)

        cast_info = []
        for item in movies:
            casts = Cast.objects.filter(movieid=item.id)
            cast_info.append(casts)
        print(cast_info)
        return render(request, 'search.html', {'movies' : movies,'q' : q, 'cast_info' : cast_info})

    else:
        return render(request, 'search.html')

def order_page(request):
    user_id = request.session.get('user')
    user_info = Customer.objects.get(pk=user_id)  #pk : primary key
    order_info = Orders.objects.filter(customerid=user_id)

    return render(request, "order.html", {'user_info' : user_info, 'order_info' : order_info})

def order(request):
    borrowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    data = request.POST['order']

    user_id = request.session.get('user')
    user_info = Customer.objects.get(pk=user_id)  #pk : primary key
    
    movie_info = Movie.objects.get(pk=data)
    movie_info.numcopies +=1
    movie_info.save()

    if not Orders.objects.filter(customerid=user_info, movieid=movie_info):
        last_order_id = Orders.objects.last()
        last_order_id = last_order_id.id
        order_id = last_order_id + 11
        Orders.objects.create(id=order_id, customerid=user_info, movieid=movie_info, borrowtime=borrowtime)
    
    order_info = Orders.objects.filter(customerid=user_id)
    return render(request, "order.html", {'user_info' : user_info, 'order_info' : order_info})


def return_order(request):
    returntime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    if len(request.POST) == 2:
        return redirect('order_page')

    data = request.POST['return_order']
    rate = request.POST['rate']

    user_id = request.session.get('user')
    user_info = Customer.objects.get(pk=user_id)  #pk : primary key
    
    movie_info = Movie.objects.get(pk=data)

    return_instance = Orders.objects.get(movieid=movie_info)
    return_instance.returntime = returntime
    return_instance.rating = rate
    return_instance.save()

    order_info = Orders.objects.filter(customerid=user_id)
    
    return render(request, "order.html", {'user_info' : user_info, 'order_info' : order_info})

