# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Product, Provider, Purchase, Departure, Inventory, Brand
from .forms import DepartureForm, PurchaseForm, InventoryForm


# Register your models here.


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id_product', 'name_product', 'category', 'description']

@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    list_display = ['id_brand', 'name_brand']


@admin.register(Provider)
class AdminProvider(admin.ModelAdmin):
    list_display = ['nit_provider', 'name_provider', 'address', 'category', 'level']



@admin.register(Purchase)
class AdminPurchase(admin.ModelAdmin):
    list_display = ['id_product', 'id_brand', 'quantity', 'cost', 'value_sale']
    form = PurchaseForm


@admin.register(Departure)
class AdminDeparture(admin.ModelAdmin):
    list_display = ['nom_product', 'id_brand', 'quantity', 'total']
    form = DepartureForm


@admin.register(Inventory)
class AdminInventory(admin.ModelAdmin):
    list_display = ['id_product', 'id_brand', 'quantity']
    form = InventoryForm



"""admin.site.register(Product, AdminProduct)
admin.site.register(Provider, AdminProduct)
admin.site.register(DetailProduct, AdminDetailProduct)
admin.site.register(DepartureInventory, AdminDepartureInventory)"""

"""admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(DetailProduct)
admin.site.register(DepartureInventory)"""