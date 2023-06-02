from django.shortcuts import render,HttpResponse ,redirect
from django.core.exceptions import ValidationError
from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.forms import UserCreationForm , User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import CreateUserForm , LoginForm


def index(request):
    return render(request, 'html/index.html')


def SignIn(request):
    form = LoginForm(request.POST)
    context = {'form' : form}
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST' and form.is_valid :
        login_form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = email , password = password)
        if user is not None :
            login(request,user)
            return redirect(index)
        else:
            login_form.add_error(None, 'Ошибка входа, попробуйте еще раз ! :-( ')
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
    logout(request)
    return redirect(index)