from django.db import models
from django.contrib.auth.models import AbstractUser , User
from phone_field import PhoneField


class UserD(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = PhoneField(blank=True, help_text='Contact phone number')
    stock = []
