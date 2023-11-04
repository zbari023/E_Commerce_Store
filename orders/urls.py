
from django.urls import path
from .views import add_to_cart , OrderList, chackout_page
from .api import CartDetailCreateDeleteAPI

app_name = 'orders'
urlpatterns = [
    path('', OrderList.as_view()),
    path('add_to_cart', add_to_cart),
    path('chackout', chackout_page),
    path('api/<str:username>/cart',CartDetailCreateDeleteAPI.as_view(),)
]