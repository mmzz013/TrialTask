from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

import random
from string import ascii_uppercase, digits


def creating_an_invite_code():
    invite_code = []
    for _ in range(6):
        random_list = [random.choice(ascii_uppercase), random.choice(digits)]
        invite_code.append(random.choice(random_list))
    return str(''.join(invite_code))


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('The phone_number must be set')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    phone_number = models.CharField(max_length=11, unique=True, blank=False)
    invite_code = models.CharField(max_length=6, default=creating_an_invite_code)
    invited_by = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    username = None
    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number