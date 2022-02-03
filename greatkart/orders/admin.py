from django.contrib import admin
from .models import Payment, Order, OrderProduct


@admin.register(Payment)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_id',
                    'amount_paid', 'status', 'created_at']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment', 'order_number', 'status', 'created_at']


@admin.register(OrderProduct)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment', 'user', 'product', 'variation']
