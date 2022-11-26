from django.urls import path

from Orders.views import MyOrders, CancelOrder,AddOrderCodes,OrderDetails

urlpatterns = [
    path('Myorders', MyOrders.as_view(), name='MyOrders'),
    path('CancelOrder/<int:pk>/', CancelOrder.as_view(), name='CancelOrder'),
    path('AddOrderCodes/<int:pk>/', AddOrderCodes.as_view(), name='AddOrderCodes'),
    path('OrderDetails/<int:pk>/', OrderDetails.as_view(), name='OrderDetails'),
    # path('UpdateOrder/<int:pk>/', UpdateOrder.as_view(), name='UpdateOrder')
]
