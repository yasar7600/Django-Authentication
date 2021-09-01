from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm

class EditUserProfile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}