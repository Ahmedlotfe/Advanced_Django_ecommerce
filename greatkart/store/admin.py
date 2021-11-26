from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price',
                    'stock', 'category', 'created_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}
