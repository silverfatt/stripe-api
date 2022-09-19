from django.conf.urls.static import static
from django.urls import path

from stripeapi import settings
from .views import item, buy_item, order, buy_order

urlpatterns = [
    path('buy/item/<int:id>/', buy_item, name='buy_item'),
    path('buy/order/<int:id>/', buy_order, name='buy_order'),
    path('item/<int:id>/', item, name='item'),
    path('order/<int:id>/', order, name='order'),
]
