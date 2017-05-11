# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']

# # coding=utf-8
#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from accounts.models import User
#
#
# class UserAdminCreationForm(UserCreationForm):
#
#     class Meta:
#         """
#         Um ModelForm tem classe Meta, a qual indica o Modelo e seus respectivos
#         campos.
#         """
#         model = User
#         fields = ['username', 'email']
#
#
# class UserAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'name', 'is_active', 'is_staff']
