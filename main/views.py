import os

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, Http404
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from .checkers import check_item_if_exist, check_order_if_exist
from .functions import *

stripe.api_key = os.environ.get('sk')
public_key = os.environ.get('pk')


def buy_item(request, id_):  # /buy/item/id
    if request.method == 'GET':
        try:
            item_to_sell = Item.objects.get(pk=id_)
        except ObjectDoesNotExist:
            raise Http404
        price = check_item_if_exist(item_to_sell)
        # Если цены на товар не существует - ошибка
        if not price:
            raise Http404
        line_items = [{'price': price, 'quantity': 1}]
        return JsonResponse(get_session_id_response(line_items, id_))


def buy_order(request, id_):  #/buy/order/id
    if request.method == 'GET':
        try:
            order_to_sell = Order.objects.get(pk=id_).order
        except ObjectDoesNotExist:
            raise Http404
        all_prices = check_order_if_exist(order_to_sell)
        # Если цен получено меньше, чем товаров в заказе - ошибка
        if len(all_prices) < len(order_to_sell):
            raise Http404
        return JsonResponse(get_session_id_response(make_order_list(order_to_sell, all_prices), id_))


def item(request: WSGIRequest, id_):  # /item/id
    if request.method == 'GET':
        try:
            item_to_sell = Item.objects.get(pk=id_)
        except ObjectDoesNotExist:
            raise Http404

        return render(request, 'main/index.html', {'item': item_to_sell, 'key': public_key, 'type': 'item'})


def order(request, id_):  # /order/id
    if request.method == 'GET':
        try:
            order_to_sell = make_items_dict(id_)
        except ObjectDoesNotExist:
            raise Http404

        return render(request, 'main/index.html', {'item': order_to_sell, 'key': public_key, 'type': 'order'})
