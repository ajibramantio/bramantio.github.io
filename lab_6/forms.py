from django import forms
from .models import Statuy
from django.forms import ModelForm


class add_status(forms.ModelForm):
    class Meta:
        model = Statuy
        fields = ["status", "isi_status"]
        widgets = {
            "status": forms.TextInput(attrs={'class': 'form-control'}),
            "isi_status": forms.TextInput(attrs={'class': 'form-control'}),
        }