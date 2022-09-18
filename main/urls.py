from django.conf.urls.static import static
from django.urls import path

from stripeapi import settings
from .views import item, buy

urlpatterns = [
    path('buy/<int:id>/', buy, name='buy'),
    path('item/<int:id>/', item, name='item'),
]
