from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phone_field import PhoneField


class UserD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    stock = []


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
    price = models.IntegerField()
    discount_price = models.IntegerField()
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
