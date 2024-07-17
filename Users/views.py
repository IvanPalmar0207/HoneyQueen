from django.shortcuts import redirect, render
#User Model
from Users.models import User
#Authenticate
from django.contrib.auth import authenticate, login, logout
#Login Function
from django.contrib.auth.decorators import login_required
#Messages
from django.contrib import messages

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
def insertUsers(request):
    pass

@login_required
def updateUsers(request):
    pass

@login_required
def deleteUsers(request):
    pass

#Manage Product
@login_required
def manageProducts(request):
    pass

@login_required
def insertProducts(request):
    pass

@login_required
def updateUsers(request):
    pass

@login_required
def deleteProducts(request):
    pass