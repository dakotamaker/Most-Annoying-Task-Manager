from django.forms import ModelForm, PasswordInput, TextInput
from . import models


class LoginForm(ModelForm):
    class Meta:
        model = models.User
        widgets = {
            'password': PasswordInput(),
        }
        fields = ['email', 'password']


class RegistrationForm(ModelForm):
    class Meta:
        model = models.User
        widgets = {
            'password': PasswordInput(),
            'user_name': TextInput(attrs={'placeholder': 'Jane Doe'}),
            'email': TextInput(attrs={'placeholder': 'janedoe@example.com'}),
            'phone_number': TextInput(attrs={'placeholder': '1234567890'}),
        }
        fields = ['user_name', 'password', 'email', 'phone_number']


class UserProfileForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['user_name', 'email', 'phone_number']
