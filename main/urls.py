from django.urls import path
from .views import item, buy_item, order, buy_order

urlpatterns = [
    path('buy/item/<int:id_>/', buy_item, name='buy_item'),
    path('buy/order/<int:id_>/', buy_order, name='buy_order'),
    path('item/<int:id_>/', item, name='item'),
    path('order/<int:id_>/', order, name='order'),
]
