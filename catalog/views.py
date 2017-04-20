# coding=utf-8

from django.shortcuts import render
from .models import Category, Product


def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)
