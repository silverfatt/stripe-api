from typing import Dict, List
from .models import Order, Item
import stripe


def make_order_dict(order_to_sell: Dict, all_prices: List):
    line_items = []
    i = 0
    for o in order_to_sell.values():
        line_items.append({
            'price': all_prices[i],
            'quantity': o['amount']
        })
        i += 1
    return line_items


def make_items_dict(id: int):
    items_to_sell = []
    order = Order.objects.get(pk=id)
    for o in order.order.values():
        items_to_sell.append((o['id'], o['amount']))
    order_to_sell = {'name': "", 'price': 0, 'id': order.id}
    for i in items_to_sell:
        item = Item.objects.get(pk=i[0])
        order_to_sell['name'] += item.name + " "
        order_to_sell['price'] += item.price
    return order_to_sell


def get_session_id_response(line_items, id):
    URL = "http://127.0.0.0:8000/"
    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=URL + 'buy/item/' + str(id),
        cancel_url=URL + 'buy/item/' + str(id),
    )
    response = {}
    response['session_id'] = checkout_session.id
    return response
