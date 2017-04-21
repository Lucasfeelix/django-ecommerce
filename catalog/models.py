# coding=utf-8

from django.db import models
from django.core.urlresolvers import reverse

"""
Models referenciam tabelas no banco de dados relacional.
Command >>> python manage.py migrate
    result busca todos os modelos dentro do nome do projeto e vai criar suas
            tabelas associadas a esses modelos.
Command >>> python manage.py makemigrations
    result gera um arquivo de migração como '001.py' após detectar que há,
    houve uma nova aplicação inserida no projeto.
"""


# models.Model modelo que representa uma tabela no banco de dados
class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:  # Meta informações acerca desse modelo
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'  # Faz com que carregue no 'Catalog'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'  # Faz com que carregue no 'Catalog'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})
