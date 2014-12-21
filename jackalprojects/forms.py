__author__ = 'cemkiy'
from django import forms
from member.models import *

class forgotten_password_form(forms.Form):
    email = forms.CharField(max_length=250)

class contact_us_form(forms.Form):
    name = forms.CharField(max_length=250, required=False)
    email = forms.CharField(max_length=250, required=False)
    title = forms.CharField(max_length=250)
    message = forms.CharField(max_length=1000)
