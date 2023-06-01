from django.db import models
from django.contrib.auth.models import AbstractUser , User
from phone_field import PhoneField


class UserD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    stock = []


class Category(models.Model):
    title = models.CharField()
    title_on_site = models.CharField()
    image = models.ImageField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField()
    hex = models.CharField()

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    title = models.CharField()
    title_on_site = models.CharField()
    vendor_code = models.CharField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.product.title
