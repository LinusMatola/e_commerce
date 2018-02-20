from django import forms
from django.contrib.auth.models import User
from .models import *

class regform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=30,
                               required=True)
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),max_length=30, required=True)

    def clean_username(self):
        uname = self.cleaned_data['username']
        try:
            match = User.objects.get(username=uname)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError('Username Already Taken')
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = User.objects.get(email=email)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError('Email ID already registered')

    def clean(self):
        password = self.cleaned_data.get("password")
        confirmpassword = self.cleaned_data["confirmpassword"]
        if password != confirmpassword:
            raise forms.ValidationError("Password did not match")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirmpassword']

# class userinfo(forms.ModelForm):
#     firstname = forms.CharField(max_length=200)
#     lastname = forms.CharField(max_length=200)
#     profile_pic = forms.FileField()
#     class Meta:
#         model=userinfo
#         fields=['firstname','lastname','profile_pic']