from django.db import models



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
    order = models.JSONField()