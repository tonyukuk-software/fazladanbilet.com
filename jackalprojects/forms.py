__author__ = 'cemkiy'
from django import forms
from member.models import *

class forgotten_password_form(forms.Form):
    email = forms.CharField(max_length=250)
