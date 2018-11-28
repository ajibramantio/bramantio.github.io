from django import forms
from .models import Subscriber

class FormSubscribe(forms.Form):
    nama = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nama Lengkap', 'id' : 'nama'}))
    email = forms.CharField(required=True, max_length=30,widget=forms.DateInput(attrs={'type': 'email', 'placeholder': 'Email', 'id' : 'email'}))
    password = forms.CharField(required=True, max_length=10,widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'id' : 'password'}))


class subs_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Subscriber
        fields = ["email", "nama", "password"]