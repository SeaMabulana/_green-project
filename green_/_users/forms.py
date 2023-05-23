from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from ._redoing import validate_password

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from za_id_number.za_id_number import (
  SouthAfricanIdentityValidate, SouthAfricanIdentityNumber)

# Create the form class.
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'za_id_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].label = ''
            self.fields[str(field)].required = False
            self.fields[str(field)].help_text = None

        self.fields['first_name'].widget.attrs.update(placeholder='First name')
        self.fields['last_name'].widget.attrs.update(placeholder='Last name')
        self.fields['za_id_number'].widget.attrs.update(placeholder='Enter your ID')
        self.fields['password1'].widget.attrs.update(placeholder='Create password')
        self.fields['password2'].widget.attrs.update(placeholder='Confirm password')
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if validate_password(password1) != True:
            # Add additional validation rules here
            raise forms.ValidationError(
                _(f'{validate_password(password1)}')
            )
        return password1
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(
                _('The two password fields didn\'t match.')
            )
        return password2

class ChangePwdForm(forms.Form):
    username = forms.CharField(
        required=False, label=False, max_length=100, widget=forms.TextInput(
            attrs={
                'class': 'input-text with-border', 
                'placeholder': 'Enter Username'
            }
        )
    )
    za_id_number = forms.CharField(
        required=False, label=False, max_length=100, widget=forms.TextInput(
            attrs={
                'class': 'input-text with-border', 
                'placeholder': 'za_id_number'
            }
        )
    )
    create_password = forms.CharField(
        required=False, 
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-text with-border', 
                'placeholder': 'Create password'
            }
        )
    )
    confirm_password = forms.CharField(
        required=False,
        label=False,
         widget=forms.PasswordInput(
            attrs={
                'class': 'input-text with-border', 
                'placeholder': 'Confirm password'
            }
        )
    )
