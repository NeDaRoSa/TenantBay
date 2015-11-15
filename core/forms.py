from django import forms
from core.models import TenantBayUser


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, min_length=8, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TenantBayUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

