from django.urls import path
#Views
from Users.views import registerUser, loginUser

urlpatterns = [
    path('registerUser/', registerUser, name = 'registerUser'),
    path('loginUsers/', loginUser, name = 'loginUsers')
]