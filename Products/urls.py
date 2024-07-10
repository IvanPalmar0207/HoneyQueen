from django.urls import path
#Views
from Products.views import seeProducts

urlpatterns = [
    path('seeProducts/<id>',seeProducts, name = 'seeProducts')
]