from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm) :
    email = forms.EmailField(max_length = 100, help_text="Enter a valid IITD E-mail address")

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data):
            raise forms.ValidationError('Account already exists with that email. Please try a different one', code='duplicate-email')
        elif 'iitd.ac.in' not in data:
            raise forms.ValidationError('Not a valid IITD E-mail', code='invalid_email')
        return data
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

