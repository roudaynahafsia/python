from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("full_name", "email", "twitter", "linkedin", "facebook", "website")








class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Champs nécessaires pour l'inscription