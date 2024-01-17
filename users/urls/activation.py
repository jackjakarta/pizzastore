from django.urls import path, include
from users.views.activation import activate_user_view, reset_token_view

app_name = 'activation'

urlpatterns = [
    path('activate/', activate_user_view, name='activate'),
    path('reset-token/', reset_token_view, name='reset_token'),
]
