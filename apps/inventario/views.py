# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.inventario.forms import PurchaseForm, DepartureForm
from apps.inventario.models import Product, Provider, Inventory, Purchase, Departure


class ListProduct(ListView):
    template_name = 'inventario/list_product.html'
    queryset = Product.objects.all()


class ListProvider(ListView):
    template_name = 'inventario/list_provider.html'
    queryset = Provider.objects.all()


class ListInventory(ListView):
    template_name = 'inventario/list_inventory.html'
    queryset = Inventory.objects.all()


class ListPurchase(ListView):
    template_name = 'inventario/list_purchase.html'
    queryset = Purchase.objects.all()


class ListDeparture(ListView):
    template_name = 'inventario/list_departure.html'
    queryset = Departure.objects.all()


class CreatePurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventario/cu_purchase.html'
    success_url = '.'


class CreateDeparture(CreateView):
    model = Purchase
    form_class = DepartureForm
    template_name = 'inventario/cu_departure.html'
    success_url = '.'

class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventario/cu_product.html'
    success_url = '.'


class CreateProvider(CreateView):
    model = ProviderForm
    form_class = DepartureForm
    template_name = 'inventario/cu_provider.html'
    success_url = '.'

# class UpdatePurchase(UpdateView):
#     model = Purchase
#     form_class = PurchaseForm
#     template_name = 'inventario/update.html'
#     success_url = '.'
#
#
# class UpdateDeparture(UpdateView):
#     model = Purchase
#     form_class = DepartureForm
#     template_name = 'inventario/update.html'
#     success_url = '.'


class DeletePurchase(DeleteView):
    model = Purchase
    template_name = 'inventario/delete.html'
    success_url = reverse_lazy('url-list')


class DeleteDeparture(DeleteView):
    model = Purchase
    template_name = 'inventario/delete.html'
    success_url = reverse_lazy('url-list')


class DeleteProvider(DeleteView):
    model = Provider
    template_name = 'inventario/delete.html'
    success_url = reverse_lazy('url-list')


class DeleteDeparture(DeleteView):
    model = Product
    template_name = 'inventario/delete.html'
    success_url = reverse_lazy('url-list')





