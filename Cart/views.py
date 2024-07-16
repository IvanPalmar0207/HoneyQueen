#Django views
from django.shortcuts import render
#Models
from Products.models import tb_products
from Users.models import User
#Login Function
from django.contrib.auth.decorators import login_required


#Choose Product View
@login_required
def chooseProduct(request, id):

    product = tb_products.objects.get(productId = id)
    User1 = request.user.documentNumber

    context = {
        'product' : product,
        'user' : User1
    }

    return render(request,'cart/chooseProduct.html', context)

#See all products
@login_required
def allProducts(request):
    return render(request, 'cart/allProducts.html')

@login_required
def selectProduct(request):
    User1 = User.get_username()

