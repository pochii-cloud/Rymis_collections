from django.urls import path

from Products.views import *

urlpatterns = [
    path('CategoryDetail/<int:pk>/', CategoryDetail.as_view(), name='CategoryDetail'),
    path('ProductList/', ProductList.as_view(), name='ProductList'),
    path('ProductDetail/<int:pk>/', ProductDetail.as_view(), name='ProductDetail'),
    path('SearchProducts/', SearchProducts.as_view(), name='SearchProducts'),
    path('FavouritesPage/', FavouritesPage.as_view(), name='FavouritesPage'),
    path('AddToFavourites/<int:pk>/', AddToFavourites.as_view(), name='AddToFavourites'),
    path('RemoveFavourite/<int:pk>/', RemoveFavourite.as_view(), name='RemoveFavourite'),

]

