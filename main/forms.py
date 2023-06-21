import phone_field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phone_field import phone_number
from django import forms

from .models import Order_list


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'password1', 'password2', 'email']


class LoginForm(forms.Form):
    email = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль')


class DeliveryForm(forms.Form):
    name = forms.CharField(label='Имя пользователя')
    phone = phone_field.PhoneField()
    email = forms.EmailField(label='Почта')
    type_of_delivery = forms.ChoiceField(choices=((1, "Нужна доставка!"), (2, "Самовывоз из шоурума"),))
    postman_code = forms.IntegerField(label='Почтовый индекс')
    city = forms.CharField(label='Город')
    street_of_sity = forms.CharField(label='Улица')
    house = forms.CharField(label='Дом')
    apartment = forms.CharField(label='Квартира/строение')
    comment = forms.Textarea()



