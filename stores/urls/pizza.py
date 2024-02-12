from django.urls import path
from stores.views.pizza import pizza_list_view

app_name = "pizza"

urlpatterns = [
    path("", pizza_list_view, name="list")
]
