from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def index(request):
    return HttpResponse('all_is_done')


def login(request):
    return render(template_name='html/login.html' , request=request)

def registration(request):
    form = CreateUserForm()
    context = {'form':form}

    if request=='POST' :
        print('1234')
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid() :
            form.save()
            return redirect('')
        else:
            return render(request, 'html/accounts/registration.html',context)



    return render(request, 'html/accounts/registration.html',context)
