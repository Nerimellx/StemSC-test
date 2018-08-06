# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .models import Human
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your views here.
class AddForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-addform'
        self.helper.form_class = 'post-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ' '
        self.helper.add_input(Submit('submit', 'Сохранить', css_class = 'main_submit'))


    class Meta:
        model = Human
        fields = ('firstName', 'lastName', 'phone_number', 'address')
