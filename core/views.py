# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product

"""
View é uma função Python que recebe um objeto requests e tem que retornar um
objeto response
"""


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'product_list.html')


def product(request):
    return render(request, 'product.html')
