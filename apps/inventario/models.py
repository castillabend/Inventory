# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name_product = models.CharField(null=False, blank=False, max_length=50)
    TYPE = (
        ('Technology', 'Technology'),
        ('Tools', 'Tools'),
        ('Foods', 'Foods'),
        ('Clothes', 'Clothes'),
        ('Shoes', 'Shoes'),
        ('Accesories', 'Accesories'),
        ('Otro', 'Otro')
    )
    category = models.CharField(choices=TYPE, null=False, blank=False, max_length=50)
    serial = models.CharField(null=True, blank=True, max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name_product


class Brand (models.Model):
    id_brand = models.AutoField(primary_key=True)
    name_brand = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name_brand


class Provider(models.Model):
    nit_provider = models.CharField(primary_key=True, max_length=50)
    name_provider = models.CharField(null=False, blank=False, max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(null=True, blank=True, max_length=50)
    phone = models.IntegerField(null=False, blank=False)
    cell_phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=50)
    TYPE = (
        ('Technology', 'Technology'),
        ('Tools', 'Tools'),
        ('Foods', 'Foods'),
        ('Clothes', 'Clothes'),
        ('Shoes', 'Shoes'),
        ('Accesories', 'Accesories'),
        ('Otro', 'Otro')
    )
    category = models.CharField(choices=TYPE, null=False, blank=False, max_length=50)

    LEVEL = (
        ('Local', 'Local'),
        ('National', 'National'),
        ('International', 'International'),
        ('Otro', 'Otro')
    )
    level = models.CharField(choices=LEVEL, null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name_provider


class Purchase(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    nit_provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    date_buy = models.DateField(null=False, blank=False)
    date_expiration = models.DateField(null=True, blank=True)
    cost = models.IntegerField(null=False, blank=False)
    value_sale = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.id_product.name_product


    """def save(self, *args, **kwargs):
        super(DetailPurchase, self).save(*args, **kwargs)
        Inventory.update_detailpurchase(self.id_product, self.quantity, self.brand)"""


class Departure(models.Model):
    id_departure = models.AutoField(primary_key=True)
    id_purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    nom_product = models.CharField(null=True, blank=True, max_length=50)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    total = models.IntegerField(null=True, blank=True)
    date_dep = models.DateField(null=True, blank=True)

    """def get_value_sale(self):
        return self.id_detail.value_sale

    def get_id_product(self):
        return self.id_detail.id_product

    def get_nom_product(self):
        return self.id_detail.id_product.name_product

    def save(self, *args, **kwargs):
        id_pro = self.id_detail.id_product
        item = Inventory.objects.filter(id_product=id_pro)
        if len(item) > 0:
            item = item[0]
            if item.quantity >= self.quantity:
                self.nom_product = self.id_detail.id_product.name_product
                self.total = self.quantity * self.id_detail.value_sale
                super(Departure, self).save(*args, **kwargs)  # Call the "real" save() method.
                Inventory.update_departure(self.id_detail.id_product, self.quantity)
        else:
            print('Product not exist in Inventary')"""


class Inventory(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)

    # def __str__(self):
    #     return self.id_inventory



    # def update_departure(id_pro, quantity_departure):
    #     item = Inventory.objects.filter(id_product=id_pro.pk)
    #     if len(item)>0:
    #         item = item[0]
    #         item.quantity -= quantity_departure
    #
    #     #else:
    #         #item = Inventory()
    #         #item.id_product = id_pro
    #         #item.quantity = 0
    #     Inventory.save(item)
    #
    # def update_detailpurchase(id_pro, quantity_detailpurchase, brand):
    #     item = Inventory.objects.filter(id_product=id_pro.pk)
    #     if len(item) > 0:
    #         item = item[0]
    #         item.quantity += quantity_detailpurchase
    #     else:
    #         item = Inventory()
    #         item.id_product = id_pro
    #         item.quantity = quantity_detailpurchase
    #     item.brand = brand
    #     Inventory.save(item)





"""
class Task(models.Model):
   progress = models.PositiveIntegerField()
   estimated_days = models.PositiveIntegerField()
   progress_X_estimated_days = models.PositiveIntegerField(editable=False)

   def save(self, *args, **kwargs):
      progress_X_estimated_days = self.progress * self.estimated_days
      super(Task, self).save(*args, **kwargs)"""