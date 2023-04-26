from products.models import Buyer,Seller
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class CreateUserForm(forms.Form):
    username = forms.EmailField()
    display_name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    contact_no = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        contact_no = cleaned_data.get('contact_no')

        if password1 and password2:
            # Only do something if both fields are valid so far.
            if password1 != password2:
                self.add_error('password2','passwords do not match')
        
        if User.objects.filter(username = username).exists():
            self.add_error('password2','User already exists')

        if len(contact_no) != 10:
            self.add_error('contact_no','Invalid Number')

        return cleaned_data


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput,validators=[validate_password])

    