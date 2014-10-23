__author__ = 'cemkiy'

from django import forms
from models import *

class new_member_form(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {'password': forms.PasswordInput(),
                   'points': forms.HiddenInput(),
                   'points_counter': forms.HiddenInput()}

class new_sale_ticket_form(forms.ModelForm):
    class Meta:
        model = On_Sales
        widgets = {'member': forms.HiddenInput()}

class edit_member_profile_form(forms.Form):
    city = forms.CharField(max_length=50)

class edit_member_password_form(forms.Form):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
