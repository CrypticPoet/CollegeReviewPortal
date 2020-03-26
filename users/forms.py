from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm) :
    email = forms.EmailField(max_length = 100, help_text="Enter a valid e-mail address")

    class Meta :
        model = User
        fields = ('username', 'email', 'password1', 'password2')