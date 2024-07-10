from django.shortcuts import render
#Models
from Products.models import tb_products

#Choose Product View
def chooseProduct(request, id):

    product = tb_products.objects.get(productId = id)

    context = {
        'product' : product
    }

    return render(request,'chooseProduct.html', context)