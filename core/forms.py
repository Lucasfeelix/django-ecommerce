# coding=utf-8
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='None')
    emai = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
