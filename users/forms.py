from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    is_staff = forms.BooleanField(label='Are you a staff member?', required = False, help_text = ('Check the box if you are.'))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'is_staff', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
