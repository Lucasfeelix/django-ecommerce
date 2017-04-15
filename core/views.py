# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

"""
View é uma função Python que recebe um objeto requests e tem que retornar um
objeto response
"""


def index(request):
    return render(request, 'index.html')
