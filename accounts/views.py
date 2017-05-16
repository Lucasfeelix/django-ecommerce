from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
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
    Classe criada para registro de usuários.

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


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """
    Classe criada para atualizar os dados do usuário.

    model = modelo a ser alterado, no caso, User;
    fields = campos a serem alterados
    """
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user


index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
