from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from accounts.forms import UserAdminCreationForm
from django.core.urlresolvers import reverse_lazy


class IndexView(LoginRequiredMixin, TemplateView):
    """
    TemplateView é outra GenericView baseada em Classe que renderiza um
    template, apenas citando o nome do template.
    """
    template_name = 'accounts/index.html'


class RegisterView(CreateView):
    """
    Variáveis:
        - template_name = template associado na chamada.
        - model = modelo de formulário que será criado com base no que foi
                  passado.
        - form_class = indica qual a classe de formulário usada.
        - success_url
    """
    template_name = 'accounts/register.html'
    model = User
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


index = IndexView.as_view()
register = RegisterView.as_view()
