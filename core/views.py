# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from catalog.models import Category, Product
from .forms import ContactForm

"""
View é uma função Python que recebe um objeto requests e tem que retornar um
objeto response
"""


def index(request):
    return render(request, 'index.html')


def contact(request):
    sucess = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        sucess = True
    context = {
        'form': form,
        'sucess': sucess,
    }
    return render(request, 'contact.html', context)

    # sucess = False
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.send_mail()
    #         sucess = True
    # else:
    #     form = ContactForm()
    # context = {
    #     'form': form,
    #     'sucess': sucess,
    # }
    # return render(request, 'contact.html', context)
