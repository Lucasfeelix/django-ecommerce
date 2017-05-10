# coding=utf-8
import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators


class User(AbstractBaseUser, UserManager):
    '''
    Modelo para sobreescrever o admin do Django.
    '''
    username = models.CharField('Username / Usuário', max_length=30,
                                unique=True, validators=[
                                    validators.RegexValidator(
                                        re.compile('^[\w.@+-]+$'),
                                        'Informe um nome de usuário válido. '
                                        'Este valor deve conter apenas letras'
                                        ', números e os caracteres: @/./+/-/_'
                                        ' .', 'invalid')
                                ], help_text='Um nome curto que será usado'
                                'para identifica=lo de forma unica na plata'
                                'forma')
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # manager por padrão, todo modelo já possui um por padrão, porém, esse
    # objects(manager) irá sobreescrever o manager padrão
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    # para exibição no admin o Django necessita do nome completo
    def get_full_name(self):
        return str(self)

    # para exibição no admin o Django necessita do nome curto
    def get_short_name(self):
        return str(self).split(' ')[0]
