from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
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


class UpdatePasswordView(LoginRequiredMixin, FormView):
    """
    UpdateView: FormView baseado por/para modelo.
    FormView: crua não possui modelo associado.
    """
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        """
        Método que pega/gera argumentos que serão passados para o formulário
        """
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()
