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

class edit_ticket_details_form(forms.ModelForm):
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
    name = forms.CharField(max_length=50, widget=forms.TextInput)
    phone = forms.CharField(max_length=11, widget=forms.TextInput)
    address = forms.CharField(max_length=256, widget=forms.TextInput)

class send_cargo_no_and_user_url_for_btc_send_form(forms.Form):
    CARGO_CHOICES = (
    (u'0', u'yurtici'),
    (u'1', u'ups'),
    (u'2', u'aras'),
    )

    cargo_company = forms.ChoiceField(choices=CARGO_CHOICES)
    cargo_no = forms.CharField(max_length=50, required=True)
    user_url_for_btc_send = forms.CharField(max_length=27, required=True)

class after_sale_complaint_form(forms.ModelForm):
    class Meta:
        model = After_Sale
        widgets = {'orders': forms.HiddenInput()}





