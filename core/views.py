# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from catalog.models import Category, Product
from .forms import ContactForm

"""
View é uma função Python que recebe um objeto requests e tem que retornar um
objeto response.
"""
User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'


index = IndexView.as_view()


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

# def get(self, request):
#     return render(request, 'index.html')

# def __call__(self, request):
#     return render(request, 'index.html')

# def index(request):
#     return render(request, 'index.html')
