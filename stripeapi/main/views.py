from django.shortcuts import render, Http404
from django.http import JsonResponse
import stripe
from stripeapi import settings
from .models import Item
from django.db.models import ObjectDoesNotExist

stripe.api_key = settings.STRIPE_SECRET_KEY
public_key = settings.STRIPE_PUBLIC_KEY


def buy(request, id):
    if request.method == 'GET':
        price = None
        URL = "http://127.0.0.0:8000/"
        item_to_sell = Item.objects.get(pk=id)

        # Получение id цены на товар
        products = stripe.Product.list()
        for product in products['data']:
            if product['name'] == item_to_sell.name and product['active']:
                id = product['id']
                prices = stripe.Price.list()
                for p in prices['data']:
                    if p['product'] == id:
                        price = p['id']
        if not price:
            raise Http404

        # Получение идентификатора сессии
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=URL + 'buy/' + str(id),
            cancel_url=URL + 'buy/' + str(id),
        )
        response = {}
        response['session_id'] = checkout_session.id
        return JsonResponse(response)


def item(request, id):
    if request.method == 'GET':
        try:
            item_to_sell = Item.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404
        return render(request, 'main\\index.html', {'item': item_to_sell, 'key': public_key})
