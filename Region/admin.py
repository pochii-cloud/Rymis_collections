from django.contrib import admin

# Register your models here.
from Region.models import Town, County

admin.site.register(County)
admin.site.register(Town)