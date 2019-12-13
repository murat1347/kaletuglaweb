from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,label="Adınız Soyadınız ",widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label="E-Posta Adresiniz",widget=forms.TextInput(attrs={'class': "form-control"}))
    title = forms.CharField(label="Konu",max_length=50,widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(label="Mesajınız",widget=forms.Textarea(attrs={'class' : 'form-control'}), required=True)