#Django views
from django.shortcuts import redirect, render
#Models
from Products.models import tb_products, tb_sizes
from Users.models import User
from Cart.models import tb_cart, tb_cartItem
#Login Function
from django.contrib.auth.decorators import login_required
#Messages
from django.contrib import messages

@login_required
def chooseProduct(request, id):

    product = tb_products.objects.get(productId = id)

    if request.user.is_authenticated:
        cart, created = tb_cart.objects.get_or_create(cartUser = request.user, cartCompleted = False)

    context = {
        'product' : product,
        'cart' : cart
    }

    return render(request,'cart/chooseProduct.html', context)

#See all products
@login_required
def allProducts(request):
    return render(request, 'cart/allProducts.html')

@login_required
def addCart(request, productId):
    if request.method == 'POST':
        sizedList = tb_sizes.objects.get(sizeId = request.POST['sizedList'])
        quantity = int(request.POST.get('counterValue', 1))
        product = tb_products.objects.get(productId = productId)

        if request.user.is_authenticated:
            cart, created = tb_cart.objects.get_or_create(cartUser = request.user, cartCompleted = False)
            cartItem, created = tb_cartItem.objects.get_or_create(cartProduct = product, cartId = cart, cartQuantity = quantity, cartSize = sizedList)

            if cartItem:
                cartItem.save()
                messages.success(request,'El producto ha sido agregado al carrito correctamente')
                return render(request,'cart/allProducts.html')
            else:
                messages.error(request,'No se ha podido agregar el producto al carrito, intenta nuevamente')
                return render(request,'cart/allProducts.html')
