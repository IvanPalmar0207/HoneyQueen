#Url Imports
from django.urls import path
#Views
from Cart.views import chooseProduct, allProducts, addCart

#Urls
urlpatterns = [
    path('chooseProduct/<id>', chooseProduct, name = 'chooseProduct'),
    path('allProducts/', allProducts, name = 'allProducts'),
    path('addCart/<productId>', addCart, name = 'addCart')
]