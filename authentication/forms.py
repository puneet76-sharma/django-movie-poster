from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms

class ProfileEditForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login' )
        labels={'email':'Email'} # because by default email showing Email Address

class ProfileAdminEditForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'} # because by default email showing Email Address