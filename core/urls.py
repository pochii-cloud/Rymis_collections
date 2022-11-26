from django.urls import path

from core.views import *

urlpatterns = [
    path('', Homepage.as_view(), name='Homepage'),
    path('ContactUs/', ContactUs.as_view(), name='ContactUs'),
    path('AddCustomerComment/', AddCustomerComment.as_view(), name='AddCustomerComment'),
]
