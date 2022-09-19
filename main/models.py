import django
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from .validators import JSONSchemaValidator, SCHEMA



class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Order(models.Model):
    order = models.JSONField(default=dict, blank=True,
                             validators=[JSONSchemaValidator(limit_value=SCHEMA)])

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Order {self.id}"

