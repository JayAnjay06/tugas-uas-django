from django import forms


class HomeForm(forms.Form):
    title = forms.CharField()
    alamat = forms.CharField()
