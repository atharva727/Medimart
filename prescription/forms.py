from django import forms
from django.contrib.auth.forms import UserCreationForm
from prescription.models import User
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Re-Enter Your Password'}),
        }