from django.conf.urls import url

from apps.inventario.views import ListPurchase, CreatePurchase, UpdatePurchase, DeletePurchase, \
    ListDeparture, CreateDeparture, UpdateDeparture, DeleteDeparture, ListProduct, ListProvider, ListInventory

urlpatterns = [
    # vistas Crear, Listar, Actualizar y Eliminar del model Purchase
    url(r'^list/purchase/$', ListPurchase.as_view(), name='list_purchase'),
    url(r'^create/purchase/$', CreatePurchase.as_view(), name='create_purchase'),
    url(r'^update/purchase/(?P<pk>[0-9]+)/$', UpdatePurchase.as_view(), name='update_purchase'),
    url(r'^delete/purchase/(?P<pk>[0-9]+)/$', DeletePurchase.as_view(), name='delete_purchase'),

    # vistas Crear, Listar, Actualizar y Eliminar del model Departure
    url(r'^list/departure/$', ListDeparture.as_view(), name='list_departure'),
    url(r'^create/departure/$', CreateDeparture.as_view(), name='create_departure'),
    url(r'^update/departure/(?P<pk>[0-9]+)/$', UpdateDeparture.as_view(), name='update_departure'),
    url(r'^delete/departure/(?P<pk>[0-9]+)/$', DeleteDeparture.as_view(), name='delete_departure'),

    # Listar inventario

    url(r'^list/provider/$', ListProvider.as_view(), name='list_provider'),


    # vistas Crear, Listar, Actualizar y Eliminar del model Product
    url(r'^list/product/$', ListProduct.as_view(), name='list_product'),
    url(r'^create/product/$', CreateProduct.as_view(), name='create_product'),
    url(r'^update/product/(?P<pk>[0-9]+)/$', UpdateProduct.as_view(), name='update_product'),
    url(r'^delete/product/(?P<pk>[0-9]+)/$', DeleteProduct.as_view(), name='delete_product'),

    # vistas Crear, Listar, Actualizar y Eliminar del model Provider
    url(r'^list/inventory/$', ListInventory.as_view(), name='list_provider'),
    url(r'^create/product/$', CreateProvider.as_view(), name='create_provider'),
    url(r'^update/product/(?P<pk>[0-9]+)/$', UpdateProvider.as_view(), name='update_provider'),
    url(r'^delete/product/(?P<pk>[0-9]+)/$', DeleteProvider.as_view(), name='delete_provider'),

]