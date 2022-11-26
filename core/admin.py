from django.contrib import admin

# Register your models here.
from core.models import Contact,CustomerComments

admin.site.register(Contact)
admin.site.register(CustomerComments)