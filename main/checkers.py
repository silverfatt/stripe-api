import stripe
from .models import Item
from typing import Dict


def check_item_if_exist(item_to_sell: Item):
    price = None
    products = stripe.Product.list()
    for product in products['data']:
        if product['name'] == item_to_sell.name and product['active']:
            prod_id = product['id']
            prices = stripe.Price.list()
            for p in prices['data']:
                if p['product'] == prod_id:
                    price = p['id']
    return price


def check_order_if_exist(order_to_sell: Dict):
    all_prices = []
    products = stripe.Product.list()
    for item in order_to_sell.values():
        item_to_sell = Item.objects.get(pk=item['id'])
        for product in products['data']:
            if product['name'] == item_to_sell.name and product['active']:
                prod_id = product['id']
                prices = stripe.Price.list()
                for p in prices['data']:
                    if p['product'] == prod_id:
                        all_prices.append(p['id'])
                        break
    return all_prices
