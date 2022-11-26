from django.urls import path

from Orders.views import MyOrders, CancelOrder
from Region.views import load_cities

urlpatterns = [
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),

]