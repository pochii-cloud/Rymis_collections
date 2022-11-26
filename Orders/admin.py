from django.contrib import admin

# Register your models here.
from Orders.models import Order, OrderCodes

admin.site.register(Order)
admin.site.register(OrderCodes)
