from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=155)
    fullname = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)

    Gender_Choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(choices=Gender_Choices, required=False, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'fullname', 'phone_number', 'gender')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.fullname = self.cleaned_data['fullname']
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        if commit:
            user.save()
        return user

class ProfileFormUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname']
