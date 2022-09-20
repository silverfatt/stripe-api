import django.db.models
from django.contrib import admin
from .models import Item, Order
import stripe


@admin.action(description='Добавить продукты в магазин')
def add_product(modeladmin, request, queryset: django.db.models.QuerySet):
    for item in queryset.all():
        product = stripe.Product.create(name=item.name)
        stripe.Price.create(product=product['id'], unit_amount=item.price, currency="usd")


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    ordering = ['name']
    actions = [add_product]
    search_fields = ('name', 'id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    ordering = ['id']
    search_fields = ('id',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
