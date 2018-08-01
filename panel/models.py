# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Human(models.Model):
    firstName = models.CharField(verbose_name = 'Имя', max_length = 64, blank = True)
    lastName = models.CharField(verbose_name = 'Фамилия', max_length = 64, blank = True)
    address = models.CharField(verbose_name = 'Адрес', max_length = 255, blank = True)
    lat = models.DecimalField(verbose_name = 'Ширина', max_digits=19, decimal_places=10, blank = True)
    lon = models.DecimalField(verbose_name='Долгота', max_digits=19, decimal_places=10, blank = True)
    phone_number = PhoneNumberField(verbose_name = 'Телефон', blank = True)

# Create your models here.
