from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import application,contact

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


class updateform(ModelForm):
    class Meta:
        model=application
        fields='__all__'
        exclude=['file1','file2']


class viewform(ModelForm):
    class Meta:
        model=application
        fields='__all__'

class contactform(ModelForm):
    class Meta:
        model=contact
        fields='__all__'