from django.contrib import admin
from . import models
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = models.ProductGallery
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price',
                    'stock', 'category', 'created_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


@admin.register(models.Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category',
                    'variation_value', 'is_active']
    list_editable = ['is_active']
    list_filter = ['product', 'variation_category', 'variation_value']


@admin.register(models.ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'created_date']


@admin.register(models.ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product']
