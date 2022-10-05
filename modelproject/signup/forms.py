from django import forms
from django.core import validators
from .models import Email

class SignupForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'