from typing import Dict, List
from .models import Order, Item
import stripe


def make_order_list(order_to_sell: Dict, all_prices: List):
    """
    Подготавливает список предметов для создания сессии
    """
    line_items = []
    i = 0
    for o in order_to_sell:
        line_items.append({
            'price': all_prices[i],
            'quantity': o['amount']
        })
        i += 1
    return line_items


def make_items_dict(id: int):
    """
    Подготавливает словарь с информацией о заказе (имя, цена, id)
    для его передачи на фронт
    """
    items_to_sell = []
    order = Order.objects.get(pk=id)
    for o in order.order:
        items_to_sell.append((o['id'], o['amount']))
    order_to_sell = {'name': f"Order {id}", 'price': 0, 'id': order.id, 'description': ""}
    for i in items_to_sell:
        item = Item.objects.get(pk=i[0])
        order_to_sell['description']  += f"{i[1]}x {item.name}     "
        order_to_sell['price'] += item.price
    return order_to_sell


def get_session_id_response(line_items, id):
    """
    Получает id сессии по id заказа/товару и списку предметов
    (в случае покупки предмета, длина line_items - 1)
    """
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
