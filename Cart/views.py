from django.shortcuts import render
#Models
from Products.models import tb_products

#Choose Product View
def chooseProduct(request, id):

    product = tb_products.objects.get(productId = id)

    context = {
        'product' : product
    }

    return render(request,'cart/chooseProduct.html', context)

#See all products
def allProducts(request):
    return render(request, 'cart/allProducts.html')