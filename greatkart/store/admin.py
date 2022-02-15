from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price',
                    'stock', 'category', 'created_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(models.Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category',
                    'variation_value', 'is_active']
    list_editable = ['is_active']
    list_filter = ['product', 'variation_category', 'variation_value']


@admin.register(models.ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    pass
