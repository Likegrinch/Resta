from django import forms
from django.forms import Textarea


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': "form-control valid"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш email', 'class': "form-control valid"}
        )
    )

    message = forms.CharField(
        min_length=20,
        widget=Textarea(
            attrs={'placeholder': 'Ваше сообщение', 'cols': 30, 'rows': 9, 'class': "form-control w-100"}
        )
    )