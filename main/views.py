import datetime
import random

from django.shortcuts import render,HttpResponse ,redirect
from django.core.exceptions import ValidationError
from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm , User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import UserD , Product , Order_list , Order_item , modal_connect, Setting
from .forms import CreateUserForm , LoginForm



def index(request):
    context = {
        'settings': Setting.objects.first(),
    }
    if request.user.is_authenticated:
        holder = check_bin(request.user.userd.stock)
        context = {
            'settings': Setting.objects.first(),
            'total_price':holder[1],
            'total_counter': holder[0],
        }
        return render(request, 'html/index.html',context = context)
    else:
        return render(request, 'html/index.html')

def SignIn(request):
    login_form = LoginForm()
    context = {'form' : login_form}
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST' :
        login_form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = email , password = password)
        if user is not None :
            login(request,user)
            return redirect(index)
        else:
            login_form.add_error('password','Ошибка входа, попробуйте еще раз ! :-( ')
            context = {'form':login_form}
            return render(request, 'html/accounts/login.html', context)
    else:
        return render(request,'html/accounts/login.html',context)


def SignUp(request):
    form = CreateUserForm()
    context = {'form':form}

    if request.method=='POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid() :
            if not User.objects.filter(email=form.cleaned_data.get('email')).exists() :
                email = form.cleaned_data.get('email')
                name = form.cleaned_data.get('first_name')
                password = form.cleaned_data.get('password1')
                new_user = User.objects.create(username=email,first_name=name,email = email , password=password)
                new_user_d = UserD.objects.create(user=new_user)
                login(request,new_user)
                messages.success(request, "Registration successful.")
                return redirect(index)
            else:
                form.add_error('email', 'Данное мыло уже занято :-(')
                context = {'form': form}
                return render(request, 'html/accounts/registration.html', context)
        else:
            context = {'form':form}
            return render(request, 'html/accounts/registration.html',context)
    return render(request, 'html/accounts/registration.html',context)

def LogOut(request):
    if request.user.is_authenticated :
        logout(request)
    else:
        return redirect(index)
    return redirect(index)

def Favorite(request):
    if request.user.is_authenticated :
        context = {'fields': ' '}
        return render(request,'html/favorite.html',context=context)
    else:
        return redirect(SignIn)

def Buy_list_check(request):

    if request.user.is_authenticated:
        data = request.user.userd.stock
        data = request.user.userd.stock
        holder = []
        holder_for_items = []
        total_price = 0
        total_count = 0
        for i in data :
            print(i['select'])
            if Product.objects.get(vendor_code= i['vender_code']):
                item = Product.objects.get(vendor_code= i['vender_code'])
                price_holder = int(item.price) * int(i['counter'])
                total_price+= price_holder
                total_count += int(i['counter'])
                holder.append({
                                'item': item ,
                                'size' : i['select'],
                                'color' : i['color'],
                                'couner' : i['counter'],
                                'vender_code' : i['vender_code'],
                                'price' : price_holder,
                               })
        print(data)
        # print(holder)
        context = {
            'item':holder ,
            'total_price': total_price ,
            'total_counter' : total_count,
                   }
    else :
        return redirect('login')
    return render(request,'html/buy_list.html',context=context)



def Buy_check(request):
    context = {

    }
    if request.user.is_anonymous:
        return redirect('index')

    bin = request.user.userd.stock
    total_price = 0
    total_count = 0
    for i in bin :
        if Product.objects.get(vendor_code=i['vender_code']):
            item = Product.objects.get(vendor_code=i['vender_code'])
            price_holder = int(item.price) * int(i['counter'])
            total_price += price_holder
            total_count += int(i['counter'])

    data = request.user.userd.stock
    holder = []
    for i in data:
        print(i['select'])
        if Product.objects.get(vendor_code=i['vender_code']):
            item = Product.objects.get(vendor_code=i['vender_code'])
            price_holder = int(item.price) * int(i['counter'])
            total_price += price_holder
            total_count += int(i['counter'])
            holder.append({
                'item': item,
                'size': i['select'],
                'color': i['color'],
                'couner': i['counter'],
                'vender_code': i['vender_code'],
                'price': int(item.price),

            })

    order_list = Order_list()



    if request.method == 'POST':
        print(request.POST['radio'])
        if request.POST['radio'] == "2" :
            name = request.POST['name']
            Phone = request.POST['phone']
            email = request.POST['email']
            postm = request.POST['postm']
            City = request.POST['City']
            street = request.POST['street']
            house = request.POST['house']
            apartments = request.POST['apartments']
            comment = request.POST['comment']

            order_list.name = name
            order_list.phone = Phone
            order_list.email = email
            order_list.post_code = postm
            order_list.City = City
            order_list.stree = street
            order_list.house = house
            order_list.appartaments = apartments
            order_list.comment = comment
            order_list.user = request.user
            order_list.type_of_delivery = '2'

            order_list.summ = total_price

            order_list.save()


            context = {
                'name ' : name ,
                'Phone' : Phone ,
                'email' : email ,
                'postm' : postm,
                'City' : City,
                'street' : street ,
                'house' : house ,
                'apartments' : apartments,
                'comment' : comment ,
            }
            for i in holder:
                order_item = Order_item(size=i['size'], price=i['price'], name=i['item'], articl=i['vender_code'],
                                        count=i['couner'], id_o=order_list, total_price = int(i['couner']) *int(i['price']),color=i['color'] )
                order_item.save()
            request.user.userd.stock = {}
            request.user.userd.save()
            return redirect('succses_d')

            # return render(request,'',context=context)
        elif request.POST['radio'] == "1" :

            name = request.POST['name']
            Phone = request.POST['phone']
            email = request.POST['email']
            context = {
                'name' : name ,
                'Phone' : Phone ,
                'email' : email ,
            }
            order_list.name = name
            order_list.email = email
            order_list.phone = Phone

            order_list.user = request.user


            order_list.save()
            # return render(request, '', context=context)
            for i in holder:
                order_item = Order_item(size=i['size'], price=i['price'], name=i['item'], articl=i['vender_code'],
                                        count=i['couner'], id_o=order_list,
                                        total_price=int(i['couner']) * int(i['price']) , color=i['color'])
                order_item.save()
            request.user.userd.stock = {}
            request.user.userd.save()
            return redirect('succses_d')
    context = {
        'total_price': total_price,
        'total_counter': total_count,
    }
    return render(request,'html/delivery_page.html',context=context)

    pass


def Category_serach(request, *args , **kwargs):
    type_of_category = request.GET.get('type_of_category')
    type_of_search = request.GET.get('type_of_search')
    object_to_q =Product.objects.get_queryset()

    print(type_of_category)

    if request.user.is_anonymous:
        return redirect('signin')

    if type_of_category!= None and(object_to_q.filter(category__product__title__contains=type_of_category) or object_to_q.filter(category__product__title_on_site__contains=type_of_category)):
        holder = check_bin(request.user.userd.stock)
        q = object_to_q.filter(category__product__title__contains=type_of_category )
        q |= object_to_q.filter(category__product__title_on_site__contains=type_of_category)
    # if(type_of_search != None):
    #     q = object_to_q.filter(category__product__title__contains=type_of_search )
    #     q |= object_to_q.filter(category__product__title_on_site__contains=type_of_search)
        print(q)
        context = {'object_to_q': q,
                   'Title_of_searching': type_of_category ,
                   # 'Title_of_category' : type_of_category
                   'total_price': holder[1],
                   'total_counter': holder[0],
                   }
        return render(request, 'html/category_serch.html', context=context)
    elif(type_of_search!=None and(object_to_q.filter(category__product__title__contains=type_of_category) or object_to_q.filter(category__product__title_on_site__contains=type_of_category))):
        holder = check_bin(request.user.userd.stock)
        q = object_to_q.filter(category__product__title__contains=type_of_search)
        q |= object_to_q.filter(category__product__title_on_site__contains=type_of_search)
        # if(type_of_search != None):
        #     q = object_to_q.filter(category__product__title__contains=type_of_search )
        #     q |= object_to_q.filter(category__product__title_on_site__contains=type_of_search)
        print(q)
        context = {'object_to_q': q,
                   'Title_of_searching': type_of_category,
                   # 'Title_of_category' : type_of_category
                   'total_price': holder[1],
                   'total_counter': holder[0],
                   }
        return render(request, 'html/category_serch.html', context=context)
    elif(type_of_search==None or type_of_category==None):
        holder = check_bin(request.user.userd.stock)
        nothing = True
        return render(request,'html/category_serch.html',context={'nothin':nothing,
                                                                  'total_price': holder[1],
                                                                  'total_counter': holder[0],
                                                                  })
    else:
        return render(request, 'html/category_serch.html', context={'nothin': True})


def Item_to_display(request,id,*args,**kwargs):
    id_of_item = id
    if id is None or Product.objects.get(category__product__vendor_code=id_of_item) is None:
        return render(request,'html/404.html')
    object_to_q = Product.objects.get(category__product__vendor_code=id_of_item)
    context = { 'i' : object_to_q }
    if request.method =="POST":
        data = request.POST
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user.userd.stock.append(data)
            user.save()
            return redirect('buy_list')
    return render(request, 'html/item_to_display.html',context=context)

def Handler_404(request):
    return render(request, 'html/404.html')

def Handler_505(request):
    return render(request,'html/505.html')

def Info(request):
    return render(request,'html/info.html')



def check_bin(data):
    total_price = 0
    total_count = 0
    for i in data:
        print(i['select'])
        if Product.objects.get(vendor_code=i['vender_code']):
            item = Product.objects.get(vendor_code=i['vender_code'])
            price_holder = int(item.price) * int(i['counter'])
            total_price += price_holder
            total_count += int(i['counter'])

    return [total_count,total_price]


def create_conn_p(request):
    if request.method == 'POST' :
        new_item = modal_connect(name=request.POST['name'],phone=request.POST['phone'],text_area=request.POST['textarea'])
        new_item.save()

    return render(request,'succsess_commit.html')
def create_conn_d(request):

    return render(request,'succsess_delivery.html')