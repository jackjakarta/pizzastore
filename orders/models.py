from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from pizzastore.models import CustomModel
from stores.models import Pizza

AuthUser = get_user_model()


class Order(CustomModel):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Pizza, through="OrderItem", related_name="orders")

    def __str__(self):
        return f"{self.user} - {self.items}"

    def __repr__(self):
        return self.__str__()


class OrderItem(CustomModel):
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="order_items")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.item} - {self.order} - {self.quantity}"

    def __repr__(self):
        return self.__str__()
