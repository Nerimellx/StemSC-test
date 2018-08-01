# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Human(models.Model):
    firstName = models.CharField(verbose_name = 'Имя', max_length = 64, blank = False)
    lastName = models.CharField(verbose_name = 'Фамилия', max_length = 64, blank = False)
    address = models.CharField(verbose_name = 'Адрес', max_length = 255, blank = False)
    lat = models.DecimalField(verbose_name = 'Ширина', max_digits=9, decimal_places=7, blank = True, null=True,default=0)
    lon = models.DecimalField(verbose_name='Долгота', max_digits=10, decimal_places=7, blank = True, null=True,default=0)
    phone_number = PhoneNumberField(verbose_name = 'Телефон', blank = False)

# Create your models here.
