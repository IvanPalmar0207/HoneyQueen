from django.urls import path
#Views
from Users.views import registerUser

urlpatterns = [
    path('registerUser/', registerUser, name = 'registerUser')
]