from django import forms
from django.contrib.auth.models import User
from .models import DuoMathUser


class DuoMathUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = DuoMathUser
        fields = ('username', 'email', 'password', 'profile_pics')
