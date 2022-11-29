from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/categories')
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField()
    image1 = models.ImageField(null=True, blank=False)
    image2 = models.ImageField(null=True, blank=False)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)
    image6 = models.ImageField(blank=True, null=True)
    image7 = models.ImageField(blank=True, null=True)
    image8 = models.ImageField(blank=True, null=True)
    image9 = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    price2 = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200, null=True)
    favourite = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


class Reviews(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    email = models.EmailField()
    review = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Reviews'
