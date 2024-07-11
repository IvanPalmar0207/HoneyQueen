#Renderation
from django.shortcuts import render
#Models
from Products.models import tb_categories

#Home View
def home(request):

    categories = tb_categories.objects.all()

    context = {
        'categories' : categories
    }

    return render(request, 'home.html', context)

#Users Login
def login(request):
    categories = tb_categories.objects.all()

    context = {
        'categories' : categories
    }

    return render(request, 'login.html', context)

#See all products
def allProducts(request):
    return render(request,'cart/allProducts.html')