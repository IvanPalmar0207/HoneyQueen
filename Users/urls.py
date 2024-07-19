from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#Views
from Users.views import registerUser, loginUser, exit
#Admin Views
#Users Management
from Users.views import manageUsers, renderInsertUser, insertUsers, renderUpdateUser, updateUsers, deleteUsers
#Products Management
from Users.views import manageProducts, renderInsertProducts, insertProducts, renderUpdateProducts, updateProducts, deleteProducts

urlpatterns = [
    path('registerUser/', registerUser, name = 'registerUser'),
    path('loginUsers/', loginUser, name = 'loginUsers'),
    path('logout/', exit, name = 'exit'),
    #Manage Users
    path('manageUsers/', manageUsers, name = 'manageUsers'),
    path('renderInsertUser/', renderInsertUser, name = 'renderInsertUser'),
    path('insertUsers/', insertUsers, name = 'insertUsers'),
    path('renderUpdateUser/<documentNumber>', renderUpdateUser, name = 'renderUpdateUser'),
    path('updateUsers/<documentNumber>', updateUsers, name = 'updateUsers'),
    path('deleteUsers/<documentNumber>', deleteUsers, name = 'deleteUsers'),
    #Manage Products
    path('manageProducts/', manageProducts, name = 'manageProducts'),
    path('renderInsertProducts/', renderInsertProducts, name = 'renderInsertProducts'),
    path('insertProducts/', insertProducts, name = 'insertProducts'),
    path('renderUpdateProducts/<productId>', renderUpdateProducts, name = 'renderUpdateProducts'),
    path('updateProducts/<productId>', updateProducts, name = 'updateProducts'),
    path('deleteProducts/<productId>', deleteProducts, name = 'deleteProducts')
]