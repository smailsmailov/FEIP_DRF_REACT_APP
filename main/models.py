import datetime
import random

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phone_field import PhoneField
from colorfield.fields import ColorField


class UserD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    phone_code = 0
    stock = []
    favorite = []

    def ganerate_sms_code(self):
        self.phone_code = random.randint(10000,99999)
        return self.phone_code


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    index = models.PositiveIntegerField()
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    building = models.CharField(max_length=32)
    apartment = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return "{0}, {1}, {2} {3}".format(self.index, self.city, self.street, self.building)


class Category(models.Model):
    title = models.CharField(max_length=32)
    title_on_site = models.CharField(max_length=32)
    image = models.ImageField(blank=True, upload_to='images/categories')
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title





class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    # size = models.ForeignKey(Size,on_delete=models.SET_NULL,null= True)
    # color  = models.ForeignKey(Color,on_delete=models.SET_NULL,null= True)
    color = models.ManyToOneRel('main.Color',to='main.Color',field_name='Color is' )
    size = models.ManyToOneRel('main.Size',to='main.Size',field_name='Size is' )
    title = models.CharField(max_length=64)
    title_on_site = models.CharField(max_length=64)
    vendor_code = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    description = models.TextField()
    compound = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=32)
    hex =  ColorField(default='#FF0000')

    def __str__(self):
        return self.title

class Image(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, upload_to='images/products')





class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = {}
    is_delivery = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()


class Menu(models.Model):
    HEADER = "HEAD"
    SIDE = "SIDE"
    FOOTER = "FOOT"
    TYPE_CHOICES = [
        (HEADER, "Header"),
        (SIDE, "Side"),
        (FOOTER, "Footer"),
    ]
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default=HEADER)
    url = models.URLField()
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Setting(models.Model):
    phone = PhoneField(blank=True)
    wa_phone = PhoneField(blank=True)
    email = models.EmailField()
    telegram = models.URLField()
    youtube = models.URLField()
    vk = models.URLField()
    instagram = models.URLField()
    avito = models.URLField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    #time
    #longitude
    #latitude

    def __str__(self):
        return "Settings"





class Order_list(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    date = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    item_detail = models.TextField(null=True)
    summ_discount = models.IntegerField(null=True)
    summ = models.IntegerField(null=True)
    SELECT = {
        ('1','Самовывоз'),
        ('2', 'Доставка'),
    }
    type_of_delivery = models.CharField(choices=SELECT, default='1', max_length=2)
    post_code = models.IntegerField(null=True)
    City = models.CharField(max_length = 100 , blank=True)
    stree = models.CharField(max_length = 100,blank=True)
    house = models.CharField(max_length = 100,blank=True)
    appartaments = models.CharField(max_length = 100,blank=True)

    comment = models.TextField(blank=True)

class Order_item(models.Model):
    id_o = models.ForeignKey(Order_list,on_delete=models.CASCADE,null = True)
    articl = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    size = models.CharField(max_length=10)
    color = ColorField(default='#FF0000')
    count = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()

    def save(self,*args, **kwargs):
        # self.total_price = self.count * self.price
        super().save(*args, **kwargs)

class modal_connect(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    text_area = models.TextField()

    def __str__(self):
        return "Обращения от          -       " + str(self.date) + self.phone

