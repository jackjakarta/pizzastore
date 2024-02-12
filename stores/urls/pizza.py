from django.urls import path
from stores.views.pizza import pizza_list_view, add_to_cart

app_name = "pizza"

urlpatterns = [
    path("", pizza_list_view, name="list"),
    path("add-to-cart/<int:pizza_id>/", add_to_cart, name="add_to_cart"),
]
