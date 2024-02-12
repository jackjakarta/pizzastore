from django.urls import path, include

from stores.views.store import StoreList

app_name = 'stores'

urlpatterns = [
    path('', StoreList.as_view(), name='list'),
    path('pizza/', include("stores.urls.pizza")),
]
