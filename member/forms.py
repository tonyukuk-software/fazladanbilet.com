__author__ = 'cemkiy'
__author__ = 'barisariburnu'
__author__ = 'kaykisizcom'


from django import forms
from models import *

class new_member_form(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {'password': forms.PasswordInput(),
                   'points': forms.HiddenInput(),
                   'points_counter': forms.HiddenInput(),
                   'profile_photo': forms.HiddenInput(), }

class new_swap_ticket_form(forms.ModelForm):
    class Meta:
        model = On_Sales
        widgets = {'member': forms.HiddenInput(),
                   'total_ticket': forms.TextInput(),
                   'amount_bitcoin': forms.TextInput()}

class edit_member_profile_form(forms.Form):
    profile_photo = forms.ImageField()

class edit_member_password_form(forms.Form):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput())

class new_order_form(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=256)




