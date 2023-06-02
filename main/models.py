from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phone_field import PhoneField


class UserD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    stock = {}


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


class Color(models.Model):
    title = models.CharField(max_length=32)
    hex = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64)
    title_on_site = models.CharField(max_length=64)
    vendor_code = models.CharField(max_length=32)
    price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images/products')

    def __str__(self):
        return self.product.title


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