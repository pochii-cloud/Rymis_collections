from django.urls import path

from Cart.views import MyCart, ManageCart, AddToCartView,CheckoutView

urlpatterns = [
    path('MyCart/', MyCart.as_view(), name='MyCart'),
    path('ManageCart/<int:cp_id>/', ManageCart.as_view(), name='ManageCart'),
    path('AddToCartView/<int:prod_id>/', AddToCartView.as_view(), name='AddToCartView'),
    path('CheckoutView/', CheckoutView.as_view(), name='CheckoutView'),
]