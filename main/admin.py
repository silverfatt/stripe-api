import django.db.models
from django.contrib import admin
from .models import Item, Order
import stripe

@admin.action(description='Добавить продукты в магазин')
def add_product(modeladmin, request, queryset: django.db.models.QuerySet):
    for item in queryset.all():
        product = stripe.Product.create(name=item.name)
        stripe.Price.create(product=product['id'], unit_amount=item.price, currency="usd")


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    ordering = ['name']
    actions = [add_product]

admin.site.register(Item,ProductAdmin)
admin.site.register(Order)
# Register your models here.
