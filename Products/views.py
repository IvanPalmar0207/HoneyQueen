from django.shortcuts import render
#Models
from Products.models import tb_products, tb_categories

#See products
def seeProducts(request, id):

    products = tb_products.objects.filter(categoryId = id)
    category = tb_categories.objects.get(categoryId = id)

    context = {
        'products' : products,
        'category' : category
    }

    return render(request,'products/products.html', context)