# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Human
from crispy_forms.helper import FormHelper
from django.shortcuts import render

# Create your views here.
class AddForm(forms.ModelForm):


    class Meta:
        model = Human
        fields = ('firstName', 'lastName', 'address', 'lat', 'lon', 'phone_number')
