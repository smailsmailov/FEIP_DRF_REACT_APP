from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['first_name','password1','password2','email']


class LoginForm(forms.Form):
    email = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль')

