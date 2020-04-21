from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

BIRTH_YEAR_CHOICES = [date for date in range(1990, 2020)]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    job = forms.CharField(label='Job', max_length=100)
    birth_date = forms.DateField(label='Date', widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    country = forms.CharField(label='Country', max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'job', 'birth_date', 'country')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
