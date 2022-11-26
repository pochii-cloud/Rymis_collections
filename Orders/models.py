from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Cart.models import Cart, CartProduct
from Region.models import County, Town

Order_Status = [
    ('delivered', 'delivered'),
    ('transit', 'transit'),
    ('pending', 'pending'),
]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=100)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=100)
    total = models.PositiveIntegerField(null=True)
    order_status = models.CharField(max_length=100, choices=Order_Status)

    def __str__(self):
        return "order" + str(self.id)

    class Meta:
        verbose_name_plural = 'Orders'


class OrderCodes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.code

