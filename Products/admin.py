from django.contrib import admin

# Register your models here.
from Products.models import Category, Products, Reviews

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Reviews)
