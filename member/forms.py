__author__ = 'cemkiy'

from django import forms
from models import *

class new_member_form(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {'password': forms.PasswordInput()}

class new_sale_ticket_form(forms.ModelForm):
    class Meta:
        model = On_Sales
        widgets = {'member': forms.HiddenInput()}

