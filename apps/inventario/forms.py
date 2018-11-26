from django import forms

from .models import Departure, Purchase, Inventory, Product, Provider


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name_product',
            'category',
            'serial',
            'description'
        ]

        labels = {
            'name_product': 'Nombre Producto',
            'category': 'Categoria',
            'serial': 'Serial',
            'description': 'Descripcion'
        }

        widgets = {
            'name_product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}),
            'category': forms.ChoiceField(),
            'serial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = [
            'nit_provider',
            'name_provider',
            'address',
            'contact',
            'phone',
            'cell_phone',
            'email',
            'category',
            'level'
        ]

        labels = {
            'nit_provider': 'NIT',
            'name_provider': 'Nombre Proveedor',
            'address': 'Direccion',
            'contact': 'Contacto',
            'phone': 'Telefono',
            'cell_phone': 'Celular',
            'email': 'Correo',
            'category': 'Categoria',
            'level': 'Nivel'
        }

        widgets = {
            'nit_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nit Proveedor'}),
            'name_provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Proveedor'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contacto'}),
            'phone': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', 'placeholder': 'Numero Fijo'}),
            'cell_phone': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', 'placeholder': 'Numero Celular'}),
            'email': forms.TextInput(),
            'category': forms.ChoiceField(),
            'level': forms.ChoiceField()
        }



class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = [#'id_purchase',
                  'id_product',
                  'id_brand',
                  'nit_provider',
                  'quantity',
                  'date_buy',
                  'date_expiration',
                  'cost',
                  'value_sale'
        ]

        labels = {
            #'id_purchase': 'ID',
            'id_product': 'Nombre de Producto',
            'id_brand': 'Marca',
            'nit_provider': 'Nombre Proveedor',
            'quantity': 'Cantidad',
            'date_buy': 'Fecha de Compra',
            'date_expiration': 'Fecha de Vencimiento',
            'cost': 'Cost',
            'value_sale': 'Precio de Venta'
        }

        widgets = {
            #'id_purchase': forms.TextInput(attrs={'class': 'form-control'}),
            'id_product': forms.Select(attrs={'class': 'form-control'}),
            'id_brand': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Marca del Producto'}),
            'nit_provider': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', }),
            'date_buy': forms.DateInput(attrs={'class': 'from-control', 'type': 'date', 'style': 'width:35%', }),
            'date_expiration': forms.DateInput(attrs={'class': 'from-control', 'type': 'date', 'style': 'width:35%', }),
            'cost': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', }),
            'value_sale': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', })
        }

    def save(self, commit=True):
        purchase = super(PurchaseForm, self).save(commit=commit)
        InventoryForm.update_purchase(purchase.id_product, purchase.quantity, purchase.id_brand)
        return purchase

    # def save(self, *args, **kwargs):
    #     super(DetailPurchaseForm, self).save(*args, **kwargs)
    #     InventoryForm.update_detailpurchase(self.id_product.pk, self.quantity, self.brand)
        # if commit:
        #     objecto.save()
        # return objecto


class DepartureForm(forms.ModelForm):
    class Meta:
        model = Departure
        fields = [
            'id_purchase',
            'nom_product',
            'id_brand',
            'quantity',
            'total',
            'date_dep'
        ]

        labels = {
            'id_purchase': 'Producto',
            'nom_product': 'Nombre de Producto',
            'id_brand': 'Marca',
            'quantity': 'Cantidad',
            'total': 'Total Salida',
            'date_dep': 'Fecha Salida'
        }

        widgets = {
            #'id_departure': forms.TextInput(attrs={'class': 'form-control'}),
            'id_purchase': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Producto y Marca'}),
            'nom_product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto'}),
            'id_brand': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Marca del Producto'}),
            'quantity': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', }),
            'total': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', }),
            'date_dep': forms.DateInput(attrs={'class': 'from-control', 'type': 'date', 'style': 'width:35%', }),
        }

    def get_value_sale(self):
        return self.id_purchase.value_sale

    def get_id_product(self):
        return self.id_purchase.id_product

    def get_nom_product(self):
        return self.id_purchase.id_product.name_product

    #def get_nom_brand(self):
        #return self.id_purchase.id_brand.name_brand

    def save(self, commit=True):

        id_pro = self.id_purchase.id_product  # self.get_id_product()
        item = Inventory.objects.filter(id_product=id_pro)
        if len(item)>0:
            item = item[0]
            if item.quantity >= self.quantity:
                self.nom_product = self.id_purchase.id_product.name_product
                self.id_brand = self.id_purchase.id_brand.name_brand
                self.total = self.quantity * self.id_purchase.value_sale
                departure = super(DepartureForm, self).save(commit=commit)
                InventoryForm.update_departure(id_pro, departure.quantity)
                return departure
        # if commit:
        #     objecto.save()
        # return objecto

        # def save(self, commit=True):
        #     purchase = super(PurchaseForm, self).save(commit=commit)
        #     InventoryForm.update_purchase(purchase.id_product, purchase.quantity, purchase.id_brand)
        #     return purchase

        # def save(self, *args, **kwargs):
        #     id_pro = self.id_detail.id_product
        #     item = Inventory.objects.filter(id_product=id_pro)
        #     if len(item) > 0:
        #         item = item[0]
        #         if item.quantity >= self.quantity:
        #             self.nom_product = self.id_detail.id_product.name_product
        #             self.total = self.quantity * self.id_detail.value_sale
        #             super(Departure, self).save(*args, **kwargs)  # Call the "real" save() method.
        #             Inventory.update_departure(self.id_detail.id_product, self.quantity)
        #     else:
        #         print('Product not exist in Inventary')
        #         """


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'id_product',
            'id_brand',
            'quantity'
        ]

        labels = {
            'id_product': 'Nombre de Producto',
            'id_brand': 'Marca',
            'quantity': 'Cantidad'
        }

        widgets = {
            'id_product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Producto y Marca'}),
            'id_brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca del Producto'}),
            'quantity': forms.NumberInput(attrs={'class': 'from-control', 'style': 'width:35%', })
        }

    def update_departure(id_pro, quantity_departure):
        item = Inventory.objects.filter(id_product=id_pro.pk)
        if len(item)>0:
            item = item[0]
            item.quantity -= quantity_departure
            item.save()

        """else:
            item = Inventory()
            item.id_product = id_pro
            item.quantity = 0"""


    def update_purchase(id_pro, quantity_purchase, id_brand):
        item = Inventory.objects.filter(id_product=id_pro.pk, id_brand=id_brand)
        if len(item)>0:
            item = item[0]
            item.quantity += quantity_purchase
        else:
            item = Inventory()
            item.id_product = id_pro
            item.id_brand = id_brand
            item.quantity = quantity_purchase
        item.save()