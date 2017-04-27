# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 3
    # a listagem de produtos dentro do Template terá o nome de 'products'
    # Como estava sendo implementado anteriormente
    # def product_list(request):
    #     context = {
    #         'product_list': Product.objects.all()
    #     }
    #     return render(request, 'catalog/product_list.html', context)


class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """
        Função que me permite adicionar uma variável ao contexto.
        """
        # super em Python é a forma de chamar a implementação anterior
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.
                                                        kwargs['slug'])
        return context
    # Como estava sendo implementado anteriormente
    # def category(request, slug):
    #     category = Category.objects.get(slug=slug)
    #     context = {
    #         'current_category': category,
    #         'product_list': Product.objects.filter(category=category)
    #     }
    #     return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)


product_list = ProductListView.as_view()
category = CategoryListView.as_view()
