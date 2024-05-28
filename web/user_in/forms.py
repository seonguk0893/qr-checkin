from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.', required=True)
    name = forms.CharField(
        max_length=255, help_text='Required. Enter your name.', required=True)
    contact = forms.CharField(
        max_length=20, help_text='Required. Enter your contact number.', required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name',
                  'contact', 'password1', 'password2')


class AuthenticationFormWithPlaceholders(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your ID'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your P/W'
