from django.urls import path
#Views
from Users.views import registerUser, loginUser, exit, manageUsers

urlpatterns = [
    path('registerUser/', registerUser, name = 'registerUser'),
    path('loginUsers/', loginUser, name = 'loginUsers'),
    path('logout/', exit, name = 'exit'),
    path('manageUsers/', manageUsers, name = 'manageUsers')
]