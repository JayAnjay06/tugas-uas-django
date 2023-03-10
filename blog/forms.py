from django.forms import ModelForm
from django import forms
from .models import blog


class ContactForm(ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

        widgets = {
            'title': forms.TextInput({'class': 'form-control'}),
            'kota': forms.TextInput({'class': 'form-control'}),
            'provinsi': forms.TextInput({'class': 'form-control'}),
        }
