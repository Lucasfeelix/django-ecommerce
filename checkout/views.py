from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from catalog.models import Product
from checkout.models import CarItem
from django.contrib import messages


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CarItem.objects.add_item(self.request.session.session_key,
                                                      product)
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso!')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso!')
        return product.get_absolute_url()


create_cartitem = CreateCartItemView.as_view()
