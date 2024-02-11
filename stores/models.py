from django.db import models
from django.contrib.auth import get_user_model
from pizzastore.models import CustomModel

AuthUser = get_user_model()


class Ingredient(CustomModel):
    name = models.CharField("Ingredients", max_length=255, unique=True)
    image = models.ImageField("Ingredient Image", upload_to="ingredients/", default=None)

    def __str__(self):
        return self.name


class Store(CustomModel):
    owner = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField("Store Name", max_length=255, unique=True)
    description = models.TextField("Store Description")
    logo = models.ImageField("Store Image", upload_to="stores/", default=None)
    delivery_fee = models.DecimalField("Delivery Fee", max_digits=5, decimal_places=2, default=0)
    profit_fee = models.DecimalField("Profit Fee", max_digits=5, decimal_places=2, default=0)
    ingredients = models.ManyToManyField(Ingredient, through="StoreIngredients", related_name='stores')

    @property
    def image_url(self):
        return self.logo.url

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class StoreIngredients(CustomModel):
    class Meta:
        verbose_name = "store ingredient"
        verbose_name_plural = "store ingredient"

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredients')
    stock = models.IntegerField(null=False, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"[{self.store}] - {self.ingredient}"

    def __repr__(self):
        return self.__str__()


class Pizza(CustomModel):
    class Meta:
        verbose_name = "pizza"
        verbose_name_plural = "pizza"

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="pizza")
    name = models.CharField("Pizza Name", max_length=255)
    image = models.ImageField("Pizza Image", upload_to="pizza/")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    ingredients = models.ManyToManyField(StoreIngredients, through="PizzaIngredients", related_name="pizza")

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return f"[{self.store}] - {self.name}"

    def __repr__(self):
        return self.__str__()


class PizzaIngredients(CustomModel):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    store_ingredient = models.ForeignKey(StoreIngredients, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f"{self.pizza} - {self.store_ingredient}"

    def __repr__(self):
        return self.__str__()


class Cart(CustomModel):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    data = models.JSONField(null=True)

    def __str__(self):
        return str(self.user)

    def __repr__(self):
        return self.__str__()
