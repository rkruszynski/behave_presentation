from django import forms
from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_staff', 'location', 'phone_number', 'phone_number2', 'phone_number3')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'placeholder': 'Password'}),
            'location': forms.TextInput(attrs={'placeholder': 'User location'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'phone_number'}),
            'phone_number2': forms.TextInput(attrs={'placeholder': 'phone_number2'}),
            'phone_number3': forms.TextInput(attrs={'placeholder': 'phone_number3'}),

        }
