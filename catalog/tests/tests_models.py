# coding=utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse
from model_mommy import mommy
from catalog.models import Category, Product


class CategoryTestCase(TestCase):
    def setUp(self):
        """
        Por que mommy.make?
        Ao invés de criarmos modelos manualmente como no exemplo abaixo:
        >>> self.category = Category.objects.create(name='', slug='', date ='')
        Usamos mommy.make() e passamos apenas o model que desejamos copiar:
        >>> self.category = mommy.make(Category) ou ('catalog.Category')
        >>> self.váriavel = mommy.make(model) ou ('api.Model')
        """
        self.category = mommy.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEqual(
            self.category.get_absolute_url(),
            reverse('catalog:category', kwargs={'slug': self.category.slug}))


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make(Product, slug='produto')

    def test_get_absolute_url(self):
        self.assertEqual(
            self.product.get_absolute_url(),
            reverse('catalog:product', kwargs={'slug': 'produto'})
        )
