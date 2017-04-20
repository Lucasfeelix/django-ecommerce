from django.contrib import admin

# Register your models here.

from .models import Category, Product


# CategoryAdmin é uma classe que vai herdar de modelAdmin
class CategoryAdmin(admin.ModelAdmin):
    # lista de campos que serão exibidos na listagem
    list_display = ['name', 'slug', 'created_at', 'modified']
    search_fields = ['name', 'slug']  # opções de buscas
    list_filter = ['created_at', 'modified']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created_at', 'modified']
    search_fields = ['name', 'slug', 'category__name']  # opções de buscas
    list_filter = ['created_at', 'modified']  # filtro lateral


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
