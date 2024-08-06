#Django views
from django.shortcuts import redirect, render
#Models
from Products.models import tb_products, tb_sizes
from Cart.models import tb_cart, tb_cartItem
from django.db.models import Sum
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

    cart = None
    cartItems = []
    
    if request.user.is_authenticated:
        cart, created = tb_cart.objects.get_or_create(cartUser = request.user, cartCompleted = False)
        cartItems = tb_cartItem.objects.filter(cartId = cart)

        total = 0
        for i in cartItems:
            total += i.price
        
        messages = f'''Los productos escogidos son:               '''
        
        products = []
        sizes = []
        for i in cartItems:            
            messages += f'{i.cartProduct.productName}, talla/s: {i.cartSize.sizeName}, {str(i.cartQuantity)} unidades, '            
            
        messages += f'                   El valor total de la compra es igual a {str(total)} COP'            
        
        context = {
            'items' : cartItems,
            'totalPrice' : total,
            'cart' : cart,
            'message' : messages,
        }

    return render(request, 'cart/allProducts.html', context)

@login_required
def addCart(request, productId):
    try:
        if request.method == 'POST':
            sizedList = tb_sizes.objects.get(sizeId = request.POST['sizedList'])
            quantity = int(request.POST.get('counterValue', 1))
            product = tb_products.objects.get(productId = productId)

            if request.user.is_authenticated:
                cart, created = tb_cart.objects.get_or_create(cartUser = request.user, cartCompleted = False)
                                    
                if product.productStock < quantity:
                    messages.error(request,'No hay unidades suficientes disponibles para confirmar la compra.')
                    return redirect('home')           
                elif product.productStock < 1:                
                    messages.error(request,'No hay unidades disponibles, espera unos momentos o trata comprando otro producto.')
                    return redirect('home')           
                        
                else:
                    cartItem, created = tb_cartItem.objects.get_or_create(cartProduct = product, cartId = cart, cartQuantity = quantity, cartSize = sizedList)
                    cartItem.save()
                    product.productStock -= quantity
                    product.save()
                    if cartItem:
                        cartItem.save()
                        messages.success(request,'El producto ha sido agregado al carrito correctamente')
                        return redirect('allProducts')       
                    messages.success(request,'El producto ha sido agregado al carrito correctamente')
                    return redirect('allProducts')                    
    except Exception:
        messages.error(request,'No se ha podido agregar el producto al carrito de compras, intenta nuevamente.')
        return redirect('home')    

@login_required
def removeCart(request, itemId):

    try:
        cartItem = tb_cartItem.objects.get(id = itemId)

        if request.user.is_authenticated:            
            product = cartItem.cartProduct
            product.productStock += cartItem.cartQuantity
            product.save()

            cartItem.delete()
            messages.success(request,'El producto ha sido eliminado correctamente del carrito de productos.')
            return redirect('home')
        else:
            messages.error(request,'No se ha podido elimianr el producto del carrito de productos, intenta nuevamente.')
            return redirect('home')
    except Exception:
        pass

@login_required
def confirmBuy(request,cartId):
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                totalPrice = request.POST['totalPrice']                
                cart = tb_cart.objects.get(cartId = cartId)
                cart.cartCompleted = True
                cart.cartTotalValue = totalPrice
                cart.save()
                messages.success(request,'La compra ha sido realizada de manera correcta, gracias y buen dia.')
                return redirect('home')
    except Exception:
        messages.error(request, 'No se ha podido finalizar tu compra, intenta neuvamente.')
        return redirect('home')