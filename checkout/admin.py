# coding=utf-8
from django.contrib import admin
from checkout.models import CartItem, Order, OrderItem


admin.site.register([CartItem, Order, OrderItem])
