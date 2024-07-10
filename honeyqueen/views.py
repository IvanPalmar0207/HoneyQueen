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

def login(request):
    categories = tb_categories.objects.all()

    context = {
        'categories' : categories
    }

    return render(request, 'login.html', context)