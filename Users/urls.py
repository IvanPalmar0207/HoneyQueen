from django.urls import path
#Views
from Users.views import registerUser, loginUser, exit

urlpatterns = [
    path('registerUser/', registerUser, name = 'registerUser'),
    path('loginUsers/', loginUser, name = 'loginUsers'),
    path('logout/', exit, name = 'exit'),
]