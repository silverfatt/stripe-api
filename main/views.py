import os

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, Http404
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from .checkers import check_item_if_exist, check_order_if_exist
from .functions import *

stripe.api_key = os.environ.get('sk')
public_key = os.environ.get('pk')



def buy_item(request, id):
    if request.method == 'GET':
        item_to_sell = Item.objects.get(pk=id)
        price = check_item_if_exist(item_to_sell)
        if not price:
            raise Http404
        line_items = [{'price': price, 'quantity': 1}]
        return JsonResponse(get_session_id_response(line_items, id))


def buy_order(request, id):
    if request.method == 'GET':
        order_to_sell = Order.objects.get(pk=id).order
        all_prices = check_order_if_exist(order_to_sell)
        if all_prices == []:
            raise Http404
        return JsonResponse(get_session_id_response(make_order_dict(order_to_sell, all_prices), id))


def item(request: WSGIRequest, id):
    if request.method == 'GET':
        try:
            item_to_sell = Item.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404

        return render(request, 'main/index.html', {'item': item_to_sell, 'key': public_key, 'type': 'item'})


def order(request, id):
    if request.method == 'GET':
        try:
            order_to_sell = make_items_dict(id)
        except ObjectDoesNotExist:
            raise Http404

        return render(request, 'main/index.html', {'item': order_to_sell, 'key': public_key, 'type': 'order'})
