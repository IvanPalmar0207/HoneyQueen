from django.shortcuts import redirect, render
#User Model
from Users.models import User
#Product Model
from Products.models import tb_products, tb_categories, tb_sizes, tb_referencies
#Authenticate
from django.contrib.auth import authenticate, login, logout
#Login Function
from django.contrib.auth.decorators import login_required
#Messages
from django.contrib import messages
#Images
from django.core.files.storage import FileSystemStorage

#Crete a new User
def registerUser(request):
    try:
        if request.method == 'POST':
            documentNumber = request.POST['documentNumber']
            namesUser = request.POST['namesUser']
            emailUser = request.POST['emailUser']
            passwordUser = request.POST['passwordUser']            

            if User.objects.filter(documentNumber = documentNumber):
                messages.info(request,'El usuario ya existe, trata de iniciar sesión.')
                return redirect(to = 'login')    

            else:
                user = User.objects.create(documentNumber = documentNumber, fullName = namesUser, email = emailUser)
                user.set_password(passwordUser)
                user.save()
                messages.success(request,'El usuario ha sido guardado correctamente.')
                return redirect(to = 'login')                     
    except:
        pass

#Login in the system
def loginUser(request):
    if request.method == 'POST':
        documentNumber = request.POST['documentNumber']
        email = request.POST['email']
        password = request.POST['password']
            
        user = authenticate(documentNumber = documentNumber, email = email, password = password)

        if user:
            login(request,user)
            messages.success(request,'Has iniciado sesión correctamente')
            return redirect('/')

        else:
            messages.error(request,'El usuario no se encuentra, intenta nuevamente')
            return redirect('/')

#Logout function
def exit(request):
    logout(request)
    messages.success(request,'Has cerrado sesión correctamente')
    return redirect('/')

#Admin Views
#Manage Users
@login_required
def manageUsers(request):
    if request.user.is_superuser:

        users = User.objects.all()

        context = {
            'users' : users
        }

        return render(request,'admin/manageUsers.html', context)
    else: 
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')
    
@login_required
def renderInsertUser(request):
    if request.user.is_superuser:
        return render(request, 'admin/newUser.html')
    else: 
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')

@login_required
def insertUsers(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            documentNumber = request.POST['documentNumber']
            namesUser = request.POST['namesUser']
            emailUser = request.POST['emailUser']
            passwordUser = request.POST['passwordUser']

            user = User.objects.create(documentNumber = documentNumber, fullName = namesUser, email = emailUser)

            if user:
                user.set_password(passwordUser)
                user.save()
                messages.success(request,'El nuevo usuario ha sido registrado correctamente, gracias.')
                return redirect('manageUsers')
            
            else:
                messages.error(request,'No se ha podido registrar al usuario correctamente, intenta nuevamente.')
                return redirect('manageUsers')
    else: 
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')

@login_required
def renderUpdateUser(request, documentNumber):
    if request.user.is_superuser:

        user = User.objects.get(documentNumber = documentNumber)

        context = {
            'user' : user
        }

        return render(request,'admin/updateUsers.html', context)
    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')        

@login_required
def updateUsers(request, documentNumber):
    if request.user.is_superuser:
        if request.method == 'POST':
            namesUser = request.POST['namesUser']
            emailUser = request.POST['emailUser']
            passwordUser = request.POST['passwordUser']

            user = User.objects.get(documentNumber = documentNumber)

            if user:
                user.fullName = namesUser
                user.email = emailUser
                user.set_password(passwordUser)

                user.save()

                messages.success(request,'El usuario ha sido actualizado correctamente, gracias.')
                return redirect('manageUsers')

            else:
                messages.error(request,'No se ha podido actualizar al usuario correctamente, intenta nuevamente.')
                return redirect('manageUsers')           

    else:
        messages.error(request, 'No tienes los permisos correspondientes')
        return redirect('home')

@login_required
def deleteUsers(request, documentNumber):
    if request.user.is_superuser:
        user = User.objects.get(documentNumber = documentNumber)

        if user:

            user.delete()      
            messages.success(request,'El ususario ha sido eliminado correctamente, gracias y buen dia.')
            return redirect('home')
        
        else:
            messages.error(request,'No se ha podido eliminar al usuario correctamente, intenta nuevamente.')
            return redirect('manageUsers')

    else:
        messages.error(request, 'No tienes los permisos correspondientes')
        return redirect('home')

#Manage Product
@login_required
def manageProducts(request):
    if request.user.is_superuser:

        products = tb_products.objects.all()

        context = {
            'products' : products
        }

        return render(request,'admin/products/manageProducts.html', context)

    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')

@login_required
def renderInsertProducts(request):
    if request.user.is_superuser:

        categories = tb_categories.objects.all()
        sizes = tb_sizes.objects.all()
        referencies = tb_referencies.objects.all()

        context = {
            'categories' : categories,
            'sizes' : sizes,
            'referencies' : referencies
        }

        return render(request,'admin/products/newProducts.html', context)
    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')

@login_required
def insertProducts(request):
    if request.user.is_superuser:
        if request.method == 'POST' and request.FILES['productImage']:
            productName = request.POST['productName']
            productDescription = request.POST['productDescription']
            productPrice = request.POST['productPrice']
            counterValue = request.POST['counterValue']
            productImage = request.FILES['productImage']

            categoryId = tb_categories.objects.get(categoryId = request.POST['categoryId'])            
            
            sizeName = [size.sizeName for size in tb_sizes.objects.all()]
            sizeId = []

            for size in sizeName:
                sizeId.append(int(request.POST.get(size))) if request.POST.get(size) else print('No se encontraron')
            

            if categoryId:

                product = tb_products.objects.create(
                    productName = productName, 
                    productDescription = productDescription, 
                    productPrice = productPrice, 
                    productStock = counterValue,
                    productImage = productImage,
                    categoryId = categoryId,
                )

                for sizedId in sizeId:
                    product.sizeId.add(tb_sizes.objects.get(sizeId = sizedId))

                product.save()

                messages.success(request,'El nuevo producto ha sido registrado correctamente, gracias.')
                return redirect('manageProducts')
            
            elif categoryId:
                
                referenceId = tb_referencies.objects.get(referenceId = request.POST['referenceId'])
                product = tb_products.objects.create(
                    productName = productName, 
                    productDescription = productDescription, 
                    productPrice = productPrice, 
                    productStock = counterValue,
                    productImage = productImage,
                    categoryId = categoryId,
                    referenceId = referenceId
                )

                for sizedId in sizeId:
                    product.sizeId.add(tb_sizes.objects.get(sizeId = sizedId))

                product.save()

                messages.success(request,'El nuevo producto ha sido registrado correctamente, gracias.')
                return redirect('manageProducts')
            
            else:
                messages.error(request,'El producto no se ha podido registrar, intenta nuevamente.')
                return redirect('manageProducts')
        else:
            pass
    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')        

@login_required
def renderUpdateProducts(request, productId):
    if request.user.is_superuser:
        product = tb_products.objects.get(productId = productId)

        categories = tb_categories.objects.all()
        referencies = tb_referencies.objects.all()
        sizes = tb_sizes.objects.all()

        context = {
            'product' : product,
            'categories' : categories,
            'referencies' : referencies,
            'sizes' : sizes
        }

        return render(request,'admin/products/updateProducts.html', context)

    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')        

@login_required
def updateProducts(request, productId):
    if request.user.is_superuser:
        
        product = tb_products.objects.get(productId = productId)

        if request.method == 'POST' and request.FILES['productImage']:

            productName = request.POST['productName']
            productDescription = request.POST['productDescription']
            productPrice = request.POST['productPrice']
            productValue = request.POST['counterValue']
            productImage = request.FILES['productImage']
            referenceId = request.POST['referenceId']

            categoryId = tb_categories.objects.get(categoryId = request.POST['categoryId'])

            sizeName = [size.sizeName for size in tb_sizes.objects.all()]
            sizeId = []

            for size in sizeName: 
                sizeId.append(int(request.POST.get(size))) if request.POST.get(size) else print('No se encontrarón')

            if referenceId == '':

                product.productName = productName
                product.productDescription = productDescription
                product.productPrice = productPrice
                product.productStock = productValue
                product.productImage = productImage
                product.categoryId = categoryId

                sizeUpdate = []
                for sizedId in sizeId:
                    sizeUpdate.append(tb_sizes.objects.get(sizeId = sizedId))

                product.sizeId.set(sizeUpdate)

                product.save()

                messages.success(request,'El producto ha sido actualizado correctamente, gracias y buen día.')
                return redirect('manageProducts')
                
            elif product:

                referenceId = tb_referencies.objects.get(referenceId = request.POST['referenceId'])

                product.productName = productName
                product.productDescription = productDescription
                product.productPrice = productPrice
                product.productStock = productValue
                product.productImage = productImage
                product.categoryId = categoryId
                product.referenceId = referenceId

                sizeUpdate = []

                for sizedId in sizeId:
                    sizeUpdate.append(tb_sizes.objects.get(sizeId = sizedId))
                
                product.sizeId.set(sizeUpdate)

                product.save()

                messages.success(request,'El producto ha sido actualizado correctamente, gracias y buen día.')
                return redirect('manageProducts')
        
            else:
                messages.error(request,'El producto no se ha podido actualizar correctamente, intenta nuevamente.')
                return redirect('manageProducts')
            
    else:        
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')


@login_required
def deleteProducts(request, productId):
    if request.user.is_superuser:        
        
        product = tb_products.objects.get(productId = productId)

        if product:

            product.delete()
            messages.success(request,'El producto ha sido eliminado correctamente, gracias y buen dia.')
            return redirect('home')
            
        else:
            messages.error(request,'No se ha podido eliminar al producto correctamente, intenta nuevamente.')
            return redirect('manageProducts')

    else:
        messages.error(request,'No tienes los permisos correspondientes')
        return redirect('home')